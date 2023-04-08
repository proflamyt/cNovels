from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')
    class Meta:
        model = Post
        fields = '__all__' 

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
        