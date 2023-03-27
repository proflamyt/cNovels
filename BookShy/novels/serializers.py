from rest_framework import serializers
from .models import NovelModel, ChapterModel, SnapShots
from authors.serializers import AuthorSerializer


class NovelSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)

    class Meta:
        model = NovelModel
        fields = ['title', 'image', 'authors']



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


class UserBookGoalSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ('user')