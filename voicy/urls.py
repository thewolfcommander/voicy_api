from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', include(admin.site.urls)),
    path('accounts/', include('accounts.urls')),
    path('posts/', include('posts.urls')),
]
