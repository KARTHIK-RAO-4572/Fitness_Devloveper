from django.urls import path
from . import views
urlpatterns = [
    path('', views.returnLandingPage, name ="Authentication Page"),
    path('signin', views.Signin, name="Sign In"),
    path('signup', views.Signup, name="Sign Up"),
]
