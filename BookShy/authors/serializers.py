from rest_framework import serializers

from .models import AuthorModel


class AuthorSerializer(serializers.ModelSerializer):
    user_image = serializers.ReadOnlyField(source='user.image.url')
    class Meta:
        model = AuthorModel
        fields = ('id', 'name', 'user_image')


