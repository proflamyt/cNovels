from rest_framework import serializers
from django.conf import settings
from novels.serializers import ChapterSerializer, NovelSerializer
from django.contrib.auth import get_user_model

User = get_user_model()





class UserSerializers(serializers.ModelSerializer):
    recently_viewed_chapters = ChapterSerializer(many=True)
    saved_novels = NovelSerializer(many=True) 
    class Meta:
        model = User
        fields = ['saved_novels', 'recently_viewed_chapters']