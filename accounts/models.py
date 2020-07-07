from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save

from voicy.utils import tools


class UserProfile(models.Model):
    """
    This would be a profile linked to the user by One-to-One Relationship.
    """
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('prefer_not_to_say', 'Prefer not to say'),
        ('custom', 'Custom')
    ]
    id = models.CharField(max_length=100, unique=True, primary_key=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES, default="male", null=True, blank=True)
    dob = models.CharField(max_length=255, null=True, blank=True, default="YYYY-MM-DD")
    profile_image = models.CharField(max_length=255, null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    tagline = models.CharField(blank=True, null=True, max_length=140)
    followers_count = models.PositiveIntegerField(null=True, blank=True, default=0)
    following_count = models.PositiveIntegerField(null=True, blank=True, default=0)
    active = models.BooleanField(default=True)
    loggedIn = models.BooleanField(default=True)
    online = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user.username)

    @property
    def followers(self):
        return self.userprofilefollower_set.all()

    
    @property
    def followers(self):
        return self.userprofilefollowing_set.all()



class UserProfileFollower(models.Model):
    """
    This will handle all the transactions related to  followers
    """
    id = models.CharField(max_length=100, unique=True, primary_key=True, blank=True)
    follower_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="follower_profile")
    follower = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    

class UserProfileFollowing(models.Model):
    """
    This will handle all the transactions related to  followers
    """
    id = models.CharField(max_length=100, unique=True, primary_key=True, blank=True)
    following_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="following_profile")
    following = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)



def pre_save_id_reciever(sender, instance, **kwargs):
    if not instance.id:
        instance.id = str(tools.random_string_generator(20)).upper()


pre_save.connect(pre_save_id_reciever, sender=UserProfile)
pre_save.connect(pre_save_id_reciever, sender=UserProfileFollower)
pre_save.connect(pre_save_id_reciever, sender=UserProfileFollowing)