from django.urls import path
from . import views


urlpatterns = [
    path('', views.returnHomePage, name="Home Page"),
    path('dashboard',views.returnDashboard, name="Dashboard"),
    path('exercise', views.returnExercisesPage, name="Exercise Page"),
    path('profile', views.returnProfilePage, name="Profile Page"),
    path('bmi', views.returnBMIPage, name="BMI Page"),
    path('exer', views.Exercise, name="Dummy"),
    path('signout', views.SignOut, name="For Signout"),
    path('change-password', views.changePassword, name="Update Password"),
    path('bicep', views.bicepCurls, name="bicep-curls"),
    path('shoulder', views.shoulderPress, name="shoulder-press"),
    path('squat', views.squat, name="squat"),

]
