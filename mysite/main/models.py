from django.db import models
from rest_framework import generics
from . import serializers
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

@login_required
class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
