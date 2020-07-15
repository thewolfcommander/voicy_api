from django.contrib.auth.models import User
from rest_framework import serializers

from accounts.models import (
    UserProfile,
    UserProfileFollower,
    ChatTransactionApprove
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


    def delete(self, instance):
        instance.follower_profile.followers_count -= 1
        instance.follower_profile.save()
        instance.follower.following_count -= 1
        instance.follower.save()
        print(instance)
        print(follower.following_count)
        print(follower_profile.follower_count)
        instance.delete()


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

    
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.password = validated_data.get('password', instance.password)
        instance.email = validated_data.get('email', instance.email)
        instance.is_active = validated_data.get('is_active', instance.is_active)

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



class ChatTransactionApproveSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatTransactionApprove
        fields = [
            'id',
            'sender',
            'reciever',
            'start_msg_id',
            'is_approved',
            'is_rejected',
            'timestamp',
            'updated',
        ]

    def update(self, instance, validated_data):
        instance.is_approved = validated_data.get('is_approved', instance.is_approved)
        instance.is_rejected = validated_data.get('is_rejected', instance.is_rejected)
        instance.save()

        return instance