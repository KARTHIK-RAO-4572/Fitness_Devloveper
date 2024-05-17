from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from . import models
from . import basepackage as bp

# Splash Page
def returnSplashPage(request):
   request.session["isAuthenticated"] = False
   return render(request,"Splash.html")

# Landing Page
def returnLandingPage(request):
    request.session["isAuthenticated"] = False
    return render(request,"Lander.html")

# Sign in
def Signin(request):
   if request.method=="POST":
      entered_email = request.POST.get('email')
      entered_password = request.POST.get('password')
      try:
         result = models.User_Data.objects.get(email=entered_email)
         actual_password = result.password
         if(actual_password==entered_password):
            obj = bp.generate_otp()
            obj.send_otp('21eg106b26@anurag.edu.in')
            request.session['isAuthenticated'] = True
            return HttpResponseRedirect('/home')
         else:
            return HttpResponse("Wrong Credentials")
      except models.User_Data.DoesNotExist:
         return HttpResponse("User Does not Exist!!")

# Signup Page
def Signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        try:
         row = models.User_Data(username=username, password=password, email=email, phone=phone) 
         row.save()
         return HttpResponseRedirect('http://localhost:8000/auth')
        except Exception as e :
           print(e)
           return HttpResponse(e)