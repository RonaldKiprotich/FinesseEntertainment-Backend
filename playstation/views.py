from django.shortcuts import render
from .serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *

# Create your views here.

class UserList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class ProfileList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        users = Profile.objects.all()
        serializer = ProfileSerializer(users, many=True)
        return Response(serializer.data)