"""Serializers for the profiles REST API."""
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from . import models

UserProfile = get_user_model()


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView."""

    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object.

    The password is accepted on write but never serialized back out, and its
    input widget is rendered as a password box by the browsable API.
    """

    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'},
            }
        }

    def create(self, validated_data):
        """Create and return a new user with a hashed password."""
        user= UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
            )
        return user
    
    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)
    
class ProfileFeeditemSerializer(serializers.ModelSerializer):
    """Serialize Profile feed items"""
    class Meta:
        model=models.ProfileFeedItem
        fields='__all__'
        extra_kwargs={
            'user_profile':{'read_only':True}
            }    
            