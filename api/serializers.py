from django.contrib.auth.models import  Group
from django.contrib.contenttypes import fields
from rest_framework import serializers
from django.contrib.auth import get_user_model
from novel.models import *

User = get_user_model()



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email","last_searched","recently_viewed_novels","saved_novels"]




class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class WeeklySerializer(serializers.ModelSerializer):
    class Meta:
        model = Weekly
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class NovelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Novel
        exclude = ['bookFile',]

class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        exclude= ['bookFile',]

class PoemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poems
        exclude =  ['bookFile', 'story']


from rest_framework_gis.serializers import GeoFeatureModelSerializer
class MapPointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = MapPoint
        geo_field = 'coord'
        id_field = False
        exclude = ('general_map',)


class NovelMapSerializer(serializers.ModelSerializer):
    general_map =  MapPointSerializer(many=True)
    class Meta:
        model = NovelMap
        geo_field = 'general_map'
        id_field=False
        exclude =('novel',)
