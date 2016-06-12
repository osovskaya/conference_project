from django import forms
from django.forms import Form, ModelForm
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from conference.models import MyUser


class UserCreationForm(ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('username', 'name', 'image')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = ('username', 'password', 'name', 'image',
                  'representative', 'conference', 'is_active', 'is_admin')

    def clean_password(self):
        return self.initial["password"]

class LoginForm(Form):
    username = forms.EmailField(max_length=50, label='Email')
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(), label='Password')
