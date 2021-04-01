from django.urls import path
from user import views

urlpatterns = [
  path("login/", views.UserAPIView.as_view({"post": "user_login"})),
  path("register/", views.UserAPIView.as_view({"post": "user_register"}))
]