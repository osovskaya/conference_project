from django.db import models
from conference.models import MyUser


class Blog(models.Model):  # one to many
    topic = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(MyUser, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.topic
