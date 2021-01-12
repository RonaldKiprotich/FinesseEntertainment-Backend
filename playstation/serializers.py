from rest_framework import serializers

from django.contrib.auth import authenticate
from .models import *

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(first_name=validated_data['first_name'], last_name=validated_data['last_name'], username=validated_data['username'], email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')
        
class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("error 400 Bad request.Invalid Details, key in the correct credentials.")

    
class BookingUserSerializer(serializers.Serializer):
  
    fullname = serializers.CharField()
    nickname = serializers.CharField()
    email = serializers.CharField()    
      
    def create(self, validated_data):
        print(request.user)
        booking = Booking(**validate_data)
        booking.save()
        return booking


class ChangePasswordSerializer(serializers.Serializer):
    """
    Serializer for password change endpoint.
    """
    model = User

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class ProfileSerializer(serializers.ModelSerializer):
    username= serializers.ReadOnlyField(source='user.username')
    email= serializers.ReadOnlyField(source='user.email')
    profilephoto= serializers.ImageField(source='user.profilephoto')
    contact= serializers.ReadOnlyField(source='user.contact')
    
    
    class Meta:
        model = Profile
        fields = ('username','email','profilephoto','contact')
        
    
