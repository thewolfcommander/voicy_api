from rest_framework import serializers

from posts.models import *


class PostCategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostCategory
        fields = (
            'id',
            'name',
            'priority',
            'timestamp'
        )


class PostMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostMedia
        fields = (
            'id',
            'media_type',
            'media_url',
            'timestamp'
        )

class PostLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLocation
        fields = (
            'id',
            'lat',
            'lng',
            'timestamp'
        )

class PostSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostSource
        fields = (
            'id',
            'media_url',
            'timestamp'
        )


class PostCreateSerializer(serializers.ModelSerializer):
    medias = PostMediaSerializer(many=True)
    sources = PostSourceSerializer(many=True)
    locations = PostLocationSerializer(many=True)
    class Meta:
        model = Post
        fields = (
            'id',
            'profile',
            'category',
            'post',
            'is_source',
            'is_verified',
            'contains_media',
            'location_added',
            'active',
            'timestamp',
            'updated',
            'medias',
            'locations',
            'sources'
        )



class PostCategoryShowSerializer(serializers.ModelSerializer):
    posts = PostCreateSerializer(many=True, read_only=True)
    class Meta:
        model = PostCategory
        fields = (
            'id',
            'name',
            'priority',
            'timestamp'
        )

    
class PostCategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostCategory
        fields = (
            'id',
            'name',
            'priority',
            'timestamp'
        )

    

class PostShowSerializer(serializers.ModelSerializer):
    medias = PostMediaSerializer(many=True, read_only=True)
    sources = PostSourceSerializer(many=True, read_only=True)
    locations = PostLocationSerializer(many=True, read_only=True)
    category = PostCategoryCreateSerializer(read_only=True)
    class Meta:
        model = Post
        fields = (
            'id',
            'profile',
            'category',
            'post',
            'is_source',
            'is_verified',
            'contains_media',
            'location_added',
            'active',
            'timestamp',
            'updated',
            'medias',
            'locations',
            'sources'
        )