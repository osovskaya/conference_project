from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib.auth import login, logout
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import FormView, View
from django.db.models import Q
from django.contrib.auth.models import Group
from datetime import datetime, timedelta
from django.utils import timezone
from django.contrib.auth.views import login

from conference.models import Conference, MyUser, Speaker
from conference.forms import LoginForm


class RegistrationView(CreateView):
    model = MyUser
    fields = ['username', 'name', 'image']
    template_name = 'conference/user_registration.html'
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


class UserProfileView(ListView):
    model = MyUser
    template_name = 'conference/user_profile.html'

    def get_queryset(self):
        self.object = get_object_or_404(MyUser, username=self.request.user.username)
        return MyUser.objects.filter(username=self.object)

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        context['user'] = self.object
        context['group'] = Group.objects.get(user=self.object)
        context['conference_list'] = self.object.conference.all()
        return context


class UserUpdateView(UpdateView):
    model = MyUser
    fields = ['name', 'image', 'conference']
    template_name = 'conference/user_update.html'
    success_url = '/conference/profile/'


class ChoseRepresentative(UpdateView):
    model = Speaker
    fields = ['speaker']
    template_name = 'conference/chose_representative.html'
    success_url = '/conference/profile/'


class ChoseSpeaker(UpdateView):
    model = Speaker
    fields = ['conference', 'speaker']
    template_name = 'conference/chose_speaker.html'
    success_url = '/conference/profile/'


class ConferenceListView(ListView):
    context_object_name = 'conference_list'
    template_name = 'conference/conference_list.html'
    paginate_by = 5

    queryset = Conference.objects.filter(end_date__gt=datetime.now()).order_by('start_date')


class ConferenceDetailView(DetailView):
    model = Conference
    context_object_name = 'conference'
    template_name = 'conference/conference_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ConferenceDetailView, self).get_context_data(**kwargs)
        context['conference'] = self.object
        group = Group.objects.get(name='listener')
        if self.object.end_date <= timezone.now():
            context['listener_list'] = MyUser.objects.filter(Q(conference=self.object), Q(groups=group))
        return context


class SponsorListView(DetailView):
    model = Conference
    template_name = 'conference/sponsor_list.html'

    def get_context_data(self, **kwargs):
        context = super(SponsorListView, self).get_context_data(**kwargs)
        context['conference'] = self.object
        group = Group.objects.get(name='company')
        context['sponsor_list'] = MyUser.objects.filter(Q(conference=self.object), Q(groups=group))
        return context


class SpeakerListView(DetailView):
    model = Conference
    template_name = 'conference/speaker_list.html'

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
