from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse, HttpResponseRedirect
from django.views.decorators import gzip
from .import Detect_Pose as dp
from authentication import models
import index
import pyttsx3
# Home Page
def returnHomePage(request):
    user = request.session["email"]
    print(user)
    if request.session["isAuthenticated"]==False:
        return HttpResponse("PERMISSION DENIED -- LOGIN FIRST!")
    return render(request,'Home.html', {'root_path':index.Root_path})

# Dashboard
def returnDashboard(request):
    if request.session["isAuthenticated"]==False:
        return HttpResponse("PERMISSION DENIED -- LOGIN FIRST!")
    return render(request,"Dashboard.html", {'root_path':index.Root_path})

# Exercises
def returnExercisesPage(request):
    if request.session["isAuthenticated"]==False:
        return HttpResponse("PERMISSION DENIED -- LOGIN FIRST!")
    return render(request,"Exercise.html", {'root_path':index.Root_path})

# BMI
def returnBMIPage(request):
    if request.session["isAuthenticated"]==False:
        return HttpResponse("PERMISSION DENIED -- LOGIN FIRST!")
    return render(request,"BMI.html", {'root_path':index.Root_path})

# Profile
def returnProfilePage(request):
    if request.session["isAuthenticated"]==False:
        return HttpResponse("PERMISSION DENIED -- LOGIN FIRST!")
    retrived_data = models.User_Data.objects.get(email = request.session['email'])
    username = retrived_data.username
    email = retrived_data.email
    phone = retrived_data.phone
    return render(request,"Profile.html",{'username':username,'email':email, 'phone':phone,'root_path':index.Root_path})

# Sign Out
def SignOut(request):
    request.session["isAuthenticated"] = False
    return HttpResponseRedirect(index.Root_path+"/auth")

#Update Password
def changePassword(request):
    if request.method == "POST":
        retrieved_data = models.User_Data.objects.get(email=request.session['email'])
        if(retrieved_data.password==request.POST.get('old-password')):
            retrieved_data.password = request.POST.get('new-password')
            retrieved_data.save()
            return HttpResponse("Password Updated Successfully!")
        else:
            return HttpResponse("Password Entered is Wrong!!")
    return HttpResponse(":::Unauthorized Access is Denied:::") 

# Exercises Start
@gzip.gzip_page
def bicepCurls(request):
    code = 1
    try:
        cam = dp.VideoCamera()
        ans = dp.gen(cam,code)
        return StreamingHttpResponse(ans, content_type="multipart/x-mixed-replace;boundary=frame")
    except:
        return HttpResponse("Sorry! An Unexpected Error Occured...")

@gzip.gzip_page
def shoulderPress(request):
    code = 2
    try:
        cam = dp.VideoCamera()
        ans = dp.gen(cam,code)
        return StreamingHttpResponse(ans, content_type="multipart/x-mixed-replace;boundary=frame")
    except:
        return HttpResponse("Sorry! An Unexpected Error Occured...")
    
@gzip.gzip_page
def squat(request):
    code = 3
    try:
        cam = dp.VideoCamera()
        ans = dp.gen(cam,code)
        return StreamingHttpResponse(ans, content_type="multipart/x-mixed-replace;boundary=frame")
    except:
        return HttpResponse("Sorry! An Unexpected Error Occured...")

def Exercise(request):
    code = int(request.GET.get('code'))
    print(code)
    return render(request, 'Integrated.html', {'code':code})