from rest_framework import serializers
from .models import NovelModel, ChapterModel, SnapShots


class NovelSerializer(serializers.ModelSerializer):

    class Meta:
        model = NovelModel
        fields = ['title', 'image', 'author__name']



class ChapterSerializer(serializers.ModelSerializer):
    book = NovelSerializer()
    class Meta:
        model = ChapterModel
        fields = ['book', 'title']


class SnapshotSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SnapShots
        fields = '__all__'


class ChapterReadSerializer(ChapterSerializer):
    content = serializers.CharField()