from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import get_object_or_404
from django.contrib.auth import login, logout
from django.views.generic.list import ListView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import FormView, View
from django.db.models import Q
from django.contrib.auth.models import Group
from datetime import datetime, timedelta
from django.utils import timezone
from django.contrib.auth.views import login

from conference.models import Conference, MyUser, Speaker, Message
from conference.forms import (LoginForm, UserCreationForm, UserChangeForm,
                              MessageCreateForm, CompanyUpdateForm,)


class RegistrationView(CreateView):
    template_name = 'conference/user_registration.html'
    form_class = UserCreationForm
    success_url = '/conference/login_page/'


class MyLoginView(FormView):
    template_name = 'conference/user_login.html'
    form_class = LoginForm

    def form_valid(self, form):
        login(self.request)
        return HttpResponseRedirect('/conference/profile/')

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class MyLogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/conference/login_page/')


class UserProfileView(ListView, CreateView):
    model = MyUser
    template_name = 'conference/user_profile.html'
    form_class = MessageCreateForm
    success_url = '/conference/profile/'

    def dispatch(self, request, *args, **kwargs):
        perms = [
            'conference.add_messages',
            'conference.add_message',
            'conference.change_message'
        ]
        if not request.user.has_perm(perms):
            return HttpResponseForbidden()
        return super(UserProfileView, self).dispatch(self, request, *args, **kwargs)

    def get_queryset(self):
        self.object = get_object_or_404(MyUser, username=self.request.user.username)
        return MyUser.objects.filter(username=self.object)

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        context['user'] = self.object
        context['group'] = Group.objects.get(user=self.object)
        context['conference_list'] = self.object.conference.all()
        context['message_list'] = Message.objects.filter(Q(sender=self.object.id) |
                                                         Q(recipient=self.object.id)).order_by('-created')
        return context


class UserUpdateView(UpdateView):
    model = MyUser
    template_name = 'conference/user_update.html'
    form_class = UserChangeForm
    success_url = '/conference/profile/'


class CompanyUpdateView(UpdateView):
    model = MyUser
    template_name = 'conference/company_update.html'
    form_class = CompanyUpdateForm
    success_url = '/conference/profile/'


class ConferenceListView(ListView):
    model = Conference
    context_object_name = 'conference_list'
    template_name = 'conference/conference_list.html'


class ConferenceDetailView(SingleObjectMixin, ListView):
    model = Conference
    context_object_name = 'conference'
    template_name = 'conference/conference_detail.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Conference.objects.all())
        return super(ConferenceDetailView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        if self.object.end_date <= timezone.now():
            return Message.objects.filter(conference=self.object)

    def get_context_data(self, **kwargs):
        context = super(ConferenceDetailView, self).get_context_data(**kwargs)
        context['conference'] = self.object
        context['message_list'] = self.get_queryset()
        return context


class SponsorListView(SingleObjectMixin, ListView):
    model = MyUser
    template_name = 'conference/sponsor_list.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('conference.view_sponsors'):
            return HttpResponseForbidden()
        return super(SponsorListView, self).dispatch(self, request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Conference.objects.all())
        return super(SponsorListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return Conference.objects.filter(id=self.object.id)

    def get_context_data(self, **kwargs):
        context = super(SponsorListView, self).get_context_data(**kwargs)
        context['conference'] = self.object
        group = Group.objects.get(name='company')
        context['sponsor_list'] = MyUser.objects.filter(Q(conference=self.object), Q(groups=group))
        return context


class SpeakerListView(SingleObjectMixin, ListView):
    model = Speaker
    template_name = 'conference/speaker_list.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Conference.objects.all())
        return super(SpeakerListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return Conference.objects.filter(id=self.object.id)

    def get_context_data(self, **kwargs):
        context = super(SpeakerListView, self).get_context_data(**kwargs)
        context['conference'] = self.object
        context['speaker_list'] = Speaker.objects.filter(conference=self.object)
        return context


class ArchieveListView(ListView):
    model = Conference
    context_object_name = 'conference_list'
    template_name = 'conference/archieve_list.html'

    def get_queryset(self):
        archieve_date = datetime.now() - timedelta(days=3)
        return Conference.objects.filter(end_date__lt=archieve_date).order_by('end_date')
