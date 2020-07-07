from django.contrib.auth.models import User
from rest_framework import generics

from accounts.models import (
    UserProfile,
    UserProfileFollower,
    UserProfileFollowing
)

from accounts.serializers import *


class RegisterUserAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserProfileCreateAPIView(generics.CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileCreateSerializer


class ListAllUsersAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserShowSerializer



class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserShowSerializer
    lookup_field = 'id'



class ListAllUserProfilesAPIView(generics.CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileShowSerializer


class UserProfileDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileShowSerializer
    lookup_field = 'id'


class FollowerAPIView(generics.CreateAPIView):
    queryset = UserProfileFollower.objects.all()
    serializer_class = UserProfileFollowerSerializer


class FollowingAPIView(generics.CreateAPIView):
    queryset = UserProfileFollowing.objects.all()
    serializer_class = UserProfileFollowingSerializer