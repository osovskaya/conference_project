from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from blog.models import Blog


class BlogListView(ListView):
    model = Blog
    context_object_name = 'blog_list'
    template_name = 'blog/blog_list.html'

class BlogDetailView(DetailView):
    model = Blog
    context_object_name = 'post'
    template_name = 'blog/blog_detail.html'
