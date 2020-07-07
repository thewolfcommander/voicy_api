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



class UserProfileShowSerializer(serializers.ModelSerializer):
    followers = UserProfileFollowerSerializer(many=True, read_only=True)
    following = UserProfileFollowingSerializer(many=True, read_only=True)
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
            'followers',
            'following'
        )
