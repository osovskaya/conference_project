from django.conf.urls import url

from blog.views import BlogListView, BlogDetailView

app_name = 'blog'
urlpatterns = [
    url(r'^$', BlogListView.as_view(), name='blog_list'),
    url(r'^(?P<pk>\d+)/$', BlogDetailView.as_view(), name='blog_detail')
]
