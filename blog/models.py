from django.db import models
from conference.models import MyUser
from django.core.urlresolvers import reverse
from swampdragon.models import SelfPublishModel


class Blog(models.Model):
    topic = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(MyUser, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('blog:blog_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.topic
