from django.contrib import admin
from .models import UserProfile,UserProfileFollower,ChatTransactionApprove

# Register your models here.
admin.site.register(ChatTransactionApprove)
admin.site.register(UserProfileFollower)
admin.site.register(UserProfile)
