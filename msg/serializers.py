from swampdragon.serializers.model_serializer import ModelSerializer


class MyUserSerializer(ModelSerializer):
    class Meta:
        model = 'conference.MyUser'
        publish_fields = ('username', 'name',)


class MessageSerializer(ModelSerializer):
    class Meta:
        model = 'msg.Message'
        publish_fields = ('content',)