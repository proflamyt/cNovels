from rest_framework import serializers

from .models import AuthorModel


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorModel
        field = ('id', 'name', 'user__image')
