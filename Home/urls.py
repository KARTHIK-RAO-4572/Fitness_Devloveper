from django.urls import path
from . import views
from . import opencv

urlpatterns = [
    path('', views.returnHomePage, name="Home Page"),
    path('dashboard',views.returnDashboard, name="Dashboard"),
    path('exercise', views.returnExercisesPage, name="Exercise Page"),
    path('profile', views.returnProfilePage, name="Profile Page"),
    path('bmi', views.returnBMIPage, name="BMI Page"),
    # path('dummy', opencv.Home, name="Dummy"),
    path('exer', views.Exercises, name="Dummy")

]
