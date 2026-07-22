from django.urls import path
from django.contrib.auth.views import LogoutView
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegisterAPIView, ProfileAPIView

urlpatterns = [
    path("register/", RegisterAPIView.as_view()),
    path("login/", obtain_auth_token),
    path("logout/", LogoutView.as_view()),
    path("profile/", ProfileAPIView.as_view()),
]