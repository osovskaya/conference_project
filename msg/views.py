from django.views.generic.edit import CreateView

from msg.models import Message


class MessageListView(CreateView):
    model = Message
    fields = ['sender', 'recipient', 'content']
    context_object_name = 'message_list'
    template_name = 'msg/message_list.html'
    success_url = '/chat/'

    def get_context_data(self, **kwargs):
        context = super(MessageListView, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
