from django.urls import path
from . import views
urlpatterns = [
    path('', views.returnLandingPage, name ="Authentication Page"),
    path('signin', views.Signin, name="Sign In"),
    path('verify-email', views.verifyEmail, name="Email Verification"),
    path('signup', views.Signup, name="Sign Up"),
]
