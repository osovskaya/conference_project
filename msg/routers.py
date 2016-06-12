from swampdragon import route_handler
from swampdragon.route_handler import ModelRouter
from msg.models import Message
from conference.models import MyUser
from msg.serializers import MyUserSerializer, MessageSerializer
from django.db.models import Q


class MyUserRouter(ModelRouter):
    route_name = 'myuser'
    serializer_class = MyUserSerializer
    model = MyUser

    def get_object(self, **kwargs):
        return self.model.objects.get(pk=kwargs['id'])

    def get_query_set(self, **kwargs):
        return self.model.objects.all()


class MessageRouter(ModelRouter):
    route_name = 'message'
    serializer_class = MessageSerializer
    model = Message
    valid_verbs = ['chat', 'subscribe', 'get_list']

    def get_object(self, **kwargs):
        return self.model.objects.get(pk=kwargs['id'])

    def get_query_set(self, **kwargs):
        return self.model.objects.filter(Q(sender=kwargs['user_id']) |
                                          Q(recipient=kwargs['user_id']))


route_handler.register(MyUserRouter)
route_handler.register(MessageRouter)


class NotificationRouter(ModelRouter):
    valid_verbs = ['subscribe']
    route_name = 'notification'
    model = Message
    serializer_class = MessageSerializer

    def get_object(self, **kwargs):
        return self.model.objects.get(pk=kwargs['pk'])

    def get_query_set(self, **kwargs):
        return self.model.objects.all()


route_handler.register(NotificationRouter)
