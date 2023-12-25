from django.urls import path
from .views import registration
from django.contrib.auth import views as auth_views

app_name = "accounts"
urlpatterns = [
    path("registration/", registration, name="registration"),
    path("login/", auth_views.LoginView.as_view(template_name="accounts/login.html"), name="login")
]