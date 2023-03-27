from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import UserIntrest
from .utils.mailer import verification_email

User = get_user_model()

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        try:
            token['profile'] = user.userintrest.profile[0]
        except:
            token['profile'] = False
        token['email_confirmed'] = user.email_confirmed
        return token
    

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(
            **validated_data
        )
        
        # user.email_user('Token', 'token') 
        return user

    class Meta:
        model = User
        fields = ('email', 'username', 'password')



class UserInterestSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = self.context["user"]
        if user.has_interest:
            raise serializers.ValidationError("User Already Registered Intrest.")
        user_interests = UserIntrest.objects.create(user=user, **validated_data)
        user.update(has_interest=True)
        return user_interests
    
    class Meta:
        model = UserIntrest
        exclude = ('user',)
        

class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def create(self, validated_data):
        user = User.objects.get(**validated_data)
        if user.email_confirmed:
            raise serializers.ValidationError('User is already verified')
        
        subject, message = verification_email(user)

        user.email_user(subject, message, html_message=message)
        
        return user