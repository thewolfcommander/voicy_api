from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from accounts.views import *

urlpatterns = [
    path('login/', obtain_auth_token),
    path('register/', RegisterUserAPIView.as_view()),
    path('create-profile/', UserProfileCreateAPIView.as_view()),
    path('users/', ListAllUsersAPIView.as_view()),
    path('users/<int:id>/', UserDetailAPIView.as_view()),
    path('profiles/', ListAllUserProfilesAPIView.as_view()),
    path('profiles/<slug:id>/', UserProfileDetailAPIView.as_view()),
    path('create-follower/', FollowerAPIView.as_view()),
    path('unfollow/<slug:id>/', UnfollowAPIView.as_view()),
    path('followers/', ListFollowerAPIView.as_view()),
]
