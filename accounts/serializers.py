from django.contrib.auth.models import User
from rest_framework import serializers

from accounts.models import (
    UserProfile,
    UserProfileFollower
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

    def create(self, validated_data):
        follower_profile = validated_data.get('follower_profile')
        follower = validated_data.get('follower')
        if follower_profile != follower:
            fp_id = UserProfile.objects.filter(id=follower_profile).first()
            fp = UserProfile.objects.filter(id=follower).first()
            fol = UserProfileFollower.objects.filter(follower=fp, follower_profile=fp_id)
            if not fol.exists():
                fp_id.followers_count += 1
                fp_id.save()
                fp.following_count += 1
                fp.save()
                instance = UserProfileFollower.objects.create(**validated_data)
            else:
                instance = validated_data
        else:
            instance = validated_data
        return instance



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


class UserProfileFollowerShowSerializer(serializers.ModelSerializer):
    follower = UserProfileCreateSerializer(read_only=True)
    follower_profile = UserProfileCreateSerializer(read_only=True)
    class Meta:
        model = UserProfileFollower
        fields = (
            'id',
            'follower_profile',
            'follower',
            'added',
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
        )

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        
        instance = validated_data
        if password is not None:
            instance = User.objects.create(**validated_data, is_active=True)
            instance.set_password(password)
            instance.save()

        return instance



class UserProfileShowSerializer(serializers.ModelSerializer):
    user = UserCreateSerializer(read_only=True)
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
