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
    medias = PostMediaSerializer(many=True, required=False)
    sources = PostSourceSerializer(many=True, required=False)
    locations = PostLocationSerializer(many=True, required=False)
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

    def create(self, validated_data):
        is_source = validated_data.get('is_source')
        if is_source:
            sources = validated_data.pop('sources', None)
            medias = validated_data.pop('medias', None)
            locations = validated_data.pop('locations', None)

            instance = Post.objects.create(
                **validated_data,
                is_verified = True
            )
            if medias is not None:
                instance.contains_media = True
                instance.save()
                for media in medias:
                    PostMedia.objects.create(**media, post=instance)

            if sources is not None:
                for source in sources:
                    PostSource.objects.create(**source, post=instance)

            if locations is not None:
                instance.location_added = True
                instance.save()
                for location in locations:
                    PostLocation.objects.create(**location, post=instance)

        else:
            medias = validated_data.pop('media', None)
            locations = validated_data.pop('locations', None)

            instance = Post.objects.create(
                **validated_data,
                is_verified = False
            )

            if medias is not None:
                instance.contains_media = True
                instance.save()
                for media in medias:
                    PostMedia.objects.create(**media, post=instance)


            if locations is not None:
                instance.location_added = True
                instance.save()
                for location in locations:
                    PostLocation.objects.create(**location, post=instance)
            
        return instance

    
    def update(self, instance, validated_data):
        sources = validated_data.pop('sources', None)
        medias = validated_data.pop('medias', None)
        locations = validated_data.pop('locations', None)

        sources_data = (instance.sources).all()
        sources_data = list(sources_data)

        medias_data = (instance.medias).all()
        medias_data = list(medias_data)

        locations_data = (instance.locations).all()
        locations_data = list(locations_data)
        
        instance.post = validated_data.get('post', instance.post)
        instance.save()

        if sources is not None:
            instance.is_verified = True
            instance.is_source = True
            instance.save()
            for source in sources:
                s = sources_data.pop(0)
                s.media_url = source.get('media_url', s.media_url)
                s.save()

        if medias is not None:
            instance.contains_media = True
            instance.save()
            for media in medias:
                m = medias_data.pop(0)
                m.media_type = media.get('media_type', m.media_type)
                m.media_url = media.get('media_url', m.media_url)
                m.save()

        if locations is not None:
            instance.location_added = True
            instance.save()
            for location in locations:
                l = locations_data.pop(0)
                l.lat = location.get('lat', l.lat)
                l.lng = location.get('lng', l.lng)
                l.save()

        return instance



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