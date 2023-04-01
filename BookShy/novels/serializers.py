from rest_framework import serializers
from .models import Goal, Marker, NovelModel, ChapterModel, SnapShots, Genre
from authors.serializers import AuthorSerializer
from rest_framework_gis.serializers import GeoFeatureModelSerializer


class NovelSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)
    genre = serializers.SlugRelatedField(slug_field='name', many=True)

    class Meta:
        model = NovelModel
        fields = ['title', 'image', 'authors', 'genre', 'ratings']


class AuthorDetailSerializer(AuthorSerializer):
    books = NovelSerializer(many=True)
    class Meta(AuthorSerializer.Meta):
        fields = ('id', 'name', 'user_image', 'books')


class ChapterSerializer(serializers.ModelSerializer):
    book = NovelSerializer()
    class Meta:
        model = ChapterModel
        fields = ['book', 'title']


class SnapshotSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SnapShots
        fields = ['image']


class ChapterReadSerializer(ChapterSerializer):
    content = serializers.CharField()

    class Meta(ChapterSerializer.Meta):
        fields = '__all__'



class UserBookGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        exclude = ('user')


class NovelMarkerSerializer(GeoFeatureModelSerializer):
    chapter = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')
    claimed_by = serializers.SlugRelatedField( read_only=True, slug_field='username')
    
    class Meta:
        model = Marker
        geo_field = "location"
        fields = ['name', 'claimed_by', 'description', 'chapter']


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'