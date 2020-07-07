from django.urls import path

from accounts.views import *

urlpatterns = [
    path('register/', RegisterUserAPIView.as_view()),
    path('create-profile/', UserProfileCreateAPIView.as_view()),
    path('users/', ListAllUsersAPIView.as_view()),
    path('users/<int:id>/', UserDetailAPIView.as_view()),
    path('profiles/', ListAllUserProfilesAPIView.as_view()),
    path('profiles/<slug:id>/', UserProfileDetailAPIView.as_view()),
    path('create-follower/', FollowerAPIView.as_view()),
    path('create-following/', FollowingAPIView.as_view()),
]