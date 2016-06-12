from django.conf.urls import url

from blog.views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView

app_name = 'blog'
urlpatterns = [
    url(r'^$', BlogListView.as_view(), name='blog_list'),
    url(r'^(?P<pk>\d+)/$', BlogDetailView.as_view(), name='blog_detail'),
    url(r'^create/$', BlogCreateView.as_view(), name='blog_create'),
    url(r'^update/(?P<pk>\d+)/$', BlogUpdateView.as_view(), name='blog_update'),
]
