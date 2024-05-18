from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse
from django.views.decorators import gzip
from . import Pose_Detection as pd 
# Home Page
def returnHomePage(request):
    user = request.session["email"]
    print(user)
    if request.session["isAuthenticated"]==False:
        return HttpResponse("PERMISSION DENIED -- LOGIN FIRST!")
    return render(request,'Home.html')

# Dashboard
def returnDashboard(request):
    if request.session["isAuthenticated"]==False:
        return HttpResponse("PERMISSION DENIED -- LOGIN FIRST!")
    return render(request,"Dashboard.html",{'Value':"Dashboard"})

# Exercises
def returnExercisesPage(request):
    if request.session["isAuthenticated"]==False:
        return HttpResponse("PERMISSION DENIED -- LOGIN FIRST!")
    return render(request,"Exercise.html")

# BMI
def returnBMIPage(request):
    if request.session["isAuthenticated"]==False:
        return HttpResponse("PERMISSION DENIED -- LOGIN FIRST!")
    return render(request,"BMI.html")

# Profile
def returnProfilePage(request):
    if request.session["isAuthenticated"]==False:
        return HttpResponse("PERMISSION DENIED -- LOGIN FIRST!")
    return render(request,"Profile.html")

# Exercises Start
@gzip.gzip_page
def Home(request):
    try:
        cam = pd.VideoCamera()
        return StreamingHttpResponse(pd.gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except:
        return HttpResponse("Sorry! An Unexpected Error Occured...")