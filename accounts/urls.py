from django.urls import path
from .views import registration, CustomLoginView, signout

app_name = "accounts"
urlpatterns = [
    path("registration/", registration, name="registration"),
    path("login/", CustomLoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("logout", signout, name="logout")
]