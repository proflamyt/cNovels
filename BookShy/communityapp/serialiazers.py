from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import GroupChat, Post, Room

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')
    class Meta:
        model = Post
        fields = '__all__' 

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
    
        
class CitizenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class RoomSerializer(serializers.ModelSerializer):
    creator = CitizenSerializer(read_only=True)
    admins = CitizenSerializer(many=True)
    class Meta:
        model = Room
        fields = '__all__'
        depth= 2
        
    def create(self, validated_data):
        validated_data['creator'] = self.context['request'].user
        return super().create(validated_data)

    



class GroupSerializer(serializers.ModelSerializer):
    citizens = CitizenSerializer(many=True)
    room = RoomSerializer()
    class Meta:
        model = GroupChat
        fields = '__all__'
        depth = 2



