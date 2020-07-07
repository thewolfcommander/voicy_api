from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save

from voicy.utils import tools
from accounts.models import UserProfile



class PostCategory(models.Model):
    """
    Model to define the different category of posts
    """
    id = models.CharField(max_length=100, blank=True, primary_key=True, unique=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    priority = models.PositiveIntegerField(default=1, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __srt__(self):
        return str(self.id)

    @property
    def posts(self):
        return self.post_set.all()



class Post(models.Model):
    """
    Model to handle the posts on the Viocy
    """
    id = models.CharField(max_length=100, blank=True, primary_key=True, unique=True)
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    category = models.ForeignKey(PostCategory, on_delete=models.CASCADE)
    post = models.CharField(max_length=255, null=True, blank=True)
    is_source = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    contains_media = models.BooleanField(default=False)
    location_added = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

    @property
    def medias(self):
        return self.postmedia_set.all()


    @property
    def locations(self):
        return self.postlocation_set.all()

    @property
    def sources(self):
        return self.postsource_set.all()


class PostMedia(models.Model):
    """
    Small model to handle post related media
    """
    MEDIA_TYPE_CHOICES = [
        ('image', "Image"),
        ('document', 'Document'),
        ('video', 'Video')
    ]
    id = models.CharField(max_length=100, blank=True, primary_key=True, unique=True)
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    media_type = models.CharField(max_length=100, choices=MEDIA_TYPE_CHOICES, default="image")
    media_url = models.URLField(null=True, blank=True, max_length=1150)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class PostSource(models.Model):
    """
    Model to handle source of proof
    """
    id = models.CharField(max_length=100, blank=True, primary_key=True, unique=True)
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    media_url = models.TextField(null=True, blank=True, max_length=1150)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    
class PostLocation(models.Model):
    """
    Model to determine location on which post is added
    """
    id = models.CharField(max_length=100, blank=True, primary_key=True, unique=True)
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    lat = models.DecimalField(max_digits=30, decimal_places=12, default=24.246461162)
    lng = models.DecimalField(max_digits=30, decimal_places=12, default=24.246461162)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


    


def pre_save_id_reciever(sender, instance, **kwargs):
    if not instance.id:
        instance.id = str(tools.random_string_generator(20)).upper()


pre_save.connect(pre_save_id_reciever, sender=PostCategory)
pre_save.connect(pre_save_id_reciever, sender=Post)
pre_save.connect(pre_save_id_reciever, sender=PostMedia)
pre_save.connect(pre_save_id_reciever, sender=PostSource)
pre_save.connect(pre_save_id_reciever, sender=PostLocation)