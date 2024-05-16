from django.urls import path
from . import views
urlpatterns = [
    path('', views.returnSplashPage, name="Root Path"),
    path('sign', views.returnLandingPage, name ="both page"),
    path('login', views.returnLoginPage, name="Login path"),
    path('signup', views.returnSignupPage, name="Signup path"),
]
