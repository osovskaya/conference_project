from django.db import models
from conference.models import MyUser
from swampdragon.models import SelfPublishModel
from msg.serializers import MessageSerializer


class Message(SelfPublishModel, models.Model):
    serializer_class = MessageSerializer
    sender = models.ForeignKey(MyUser, on_delete=models.DO_NOTHING, related_name='sender')
    recipient = models.ForeignKey(MyUser, on_delete=models.DO_NOTHING, related_name='recipient')
    content = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
