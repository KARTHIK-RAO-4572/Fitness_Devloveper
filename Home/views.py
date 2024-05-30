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
    obj1 = pyttsx3.init()
    obj1.setProperty('voice', 'en-UK')
    obj1.setProperty("rate", 155)
    obj1.say("You now Chose Bicep Curls!")
    obj1.say("Consistently performing the bicep curl will help you build strength in the upper arm and learn to use your arm muscles correctly, bracing with your core muscles.")
    obj1.say("Come on. Lets start the exercise in")
    obj1.say("three")
    obj1.say("two")
    obj1.say("one")
    obj1.say("Go")
    obj1.runAndWait()
    try:
        cam = dp.VideoCamera()
        ans = dp.gen(cam,code)
        return StreamingHttpResponse(ans, content_type="multipart/x-mixed-replace;boundary=frame")
    except:
        return HttpResponse("Sorry! An Unexpected Error Occured...")

@gzip.gzip_page
def shoulderPress(request):
    code = 2
    obj1 = pyttsx3.init()
    obj1.setProperty('voice', 'en-UK')
    obj1.setProperty("rate", 155)
    obj1.say("You now chose Shoulder press!")
    obj1.say("Shoulder press targets your shoulders, triceps, and upper back muscles, providing a full upper body workout. ")
    obj1.say("It mainly increases the muscle mass, improved posture and shoulder strength & stability.")
    obj1.say("Come on. Lets start the exercise in")
    obj1.say("three")
    obj1.say("two")
    obj1.say("one")
    obj1.say("Go")
    obj1.runAndWait()
    
    try:
        cam = dp.VideoCamera()
        ans = dp.gen(cam,code)
        return StreamingHttpResponse(ans, content_type="multipart/x-mixed-replace;boundary=frame")
    except:
        return HttpResponse("Sorry! An Unexpected Error Occured...")
    
@gzip.gzip_page
def squat(request):
    code = 3
    obj1 = pyttsx3.init()
    obj1.setProperty('voice', 'en-UK')
    obj1.setProperty("rate", 155)
    obj1.say("You now chose Squatss!")
    obj1.say("Squats are a functional exercise that can boost your calorie burn, help prevent injuries, strengthen your core, and improve your balance and posture.")
    obj1.say("Come on. Lets start the exercise in")
    obj1.say("three")
    obj1.say("two")
    obj1.say("one")
    obj1.say("Go")
    obj1.runAndWait()
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