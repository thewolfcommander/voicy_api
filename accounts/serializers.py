from django.contrib.auth.models import User
from rest_framework import serializers

from accounts.models import (
    UserProfile,
    UserProfileFollower,
    UserProfileFollowing
)


class UserProfileFollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfileFollower
        fields = (
            'id',
            'follower_profile',
            'follower',
            'added'
        )


class UserProfileFollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfileFollowing
        fields = (
            'id',
            'following_profile',
            'following',
            'added'
        )


class UserProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = (
            'id',
            'user',
            'gender',
            'dob',
            'profile_image',
            'bio',
            'tagline',
            'followers_count',
            'following_count',
            'active',
            'loggedIn',
            'online',
            'timestamp',
            'updated',
        )


class UserProfileShowSerializer(serializers.ModelSerializer):
    followers = UserProfileFollowerSerializer(many=True, read_only=True)
    following = UserProfileFollowingSerializer(many=True, read_only=True)
    class Meta:
        model = UserProfile
        fields = (
            'id',
            'gender',
            'dob',
            'profile_image',
            'bio',
            'tagline',
            'followers_count',
            'following_count',
            'active',
            'loggedIn',
            'online',
            'timestamp',
            'updated',
            'followers',
            'following'
        )



class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'password',
            'email',
            'is_active',
            'is_admin',
            'is_staff',
        )


class UserShowSerializer(serializers.ModelSerializer):
    user_profile = UserProfileShowSerializer(read_only=True)
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'password',
            'email',
            'is_active',
            'is_admin',
            'is_staff',
            'user_profile'
        )