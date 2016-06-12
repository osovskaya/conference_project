from django.conf.urls import url

from msg.views import MessageListView

app_name = 'chat'
urlpatterns = [
    url(r'^$', MessageListView.as_view(), name='message_list'),
]
