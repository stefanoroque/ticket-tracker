from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("signin", views.signin_view, name="signin"),
    path("register", views.register, name="register"),
    path("signout", views.signout, name="signout")
]