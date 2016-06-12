from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^conference/', include('conference.urls', namespace='conference')),
    url(r'^chat/', include('msg.urls', namespace='chat')),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'static'}),
]
