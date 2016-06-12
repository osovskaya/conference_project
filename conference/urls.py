from django.conf.urls import url

from conference.views import ConferenceListView, ConferenceDetailView, SponsorListView,\
    ArchieveListView, SpeakerListView, UserProfileView, MyLoginView, MyLogoutView, \
    UserUpdateView, RegistrationView, ChoseRepresentative, ChoseSpeaker

app_name = 'conference'
urlpatterns = [
    url(r'^profile/$', UserProfileView.as_view(), name='user_detail'),
    url(r'^user_update/(?P<pk>\d+)/$', UserUpdateView.as_view(), name='user_update'),
    url(r'^chose_representative/(?P<pk>\d+)/$', ChoseRepresentative.as_view(), name='chose_representative'),
    url(r'^chose_speaker/(?P<pk>\d+)/$', ChoseSpeaker.as_view(), name='chose_speaker'),
    url(r'^login_page/$', MyLoginView.as_view(), name='login_page'),
    url(r'^logout_page/$', MyLogoutView.as_view(), name='logout_page'),
    url(r'^registration/$', RegistrationView.as_view(), name='registration'),


    url(r'^(?P<pk>\d+)/sponsors/$', SponsorListView.as_view(), name='sponsor_list'),
	url(r'^(?P<pk>\d+)/speakers/$', SpeakerListView.as_view(), name='speaker_list'),

    url(r'^$', ConferenceListView.as_view(), name='conference_list'),
    url(r'^(?P<pk>\d+)/$', ConferenceDetailView.as_view(), name='conference_detail'),
    url(r'^archieve/$', ArchieveListView.as_view(), name='archieve_list'),
]
