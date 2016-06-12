from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from blog.models import Blog


class BlogListView(ListView):
    model = Blog
    context_object_name = 'blog_list'
    template_name = 'blog/blog_list.html'
    paginate_by = 5

class BlogDetailView(DetailView):
    model = Blog
    context_object_name = 'post'
    template_name = 'blog/blog_detail.html'

class BlogCreateView(CreateView):
    model = Blog
    fields = ['topic', 'content', 'author']
    template_name = 'blog/blog_create.html'

class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['topic', 'content']
    template_name = 'blog/blog_update.html'

class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog_list')
