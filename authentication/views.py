from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from . import models


# Splash Page
def returnSplashPage(request):
   return render(request,"Splash.html")

# Landing Page
def returnLandingPage(request):
    return render(request,"Lander.html")

# Login Page
def returnLoginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if(username=="karthik" and password=="zumka"):
            return HttpResponseRedirect('/home')
        else:
            return HttpResponse("Wrong Credentials")
    else:
      return render(request,"Login.html")

# Signup Page
def returnSignupPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        try:
         row = models.User_Data(username=username, password=username, email=email, phone=phone) 
         row.save()
         return HttpResponseRedirect('auth/sign')
        except Exception as e :
           print(e)
           return HttpResponse(e)