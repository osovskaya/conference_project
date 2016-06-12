from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from conference.forms import UserChangeForm, UserCreationForm
from conference.models import MyUser, Conference, Speaker


@admin.register(MyUser)
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('username', 'name', 'image', 'representative', 'created', 'is_admin')
    list_filter = ('is_admin', )
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('image', 'name', 'conference')}),
        ('Permissions', {'fields': ('is_admin', 'groups')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'name', 'image', 'password1', 'password2')}),
    )
    search_fields = ('username', 'name')
    ordering = ('username',)
    filter_horizontal = ()


@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    list_display = ('speaker', 'conference')


@admin.register(Conference)
class ConferenceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'start_date', 'end_date')
