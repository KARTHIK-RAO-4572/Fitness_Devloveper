from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from . import models
from . import basepackage as bp
import index
# Reference Class
class Reference():
   OTP = None
   email = None
   password = None
   username = None
   phone = None

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
            request.session['isAuthenticated'] = True
            request.session['email'] = entered_email
            return HttpResponseRedirect('/home')
         else:
            return HttpResponse("Wrong Credentials")
      except models.User_Data.DoesNotExist:
         return HttpResponse("User Does not Exist!!")
   else:
      return HttpResponse(":::Unauthorized Access is Denied:::")

#Verify Email
def verifyEmail(request):
   if request.method == "POST":
      Reference.email = request.POST.get('email')
      Reference.username = request.POST.get('username')
      Reference.password = request.POST.get('password')
      Reference.phone = request.POST.get('phone')
      obj = bp.generate_otp()
      try:
         result = models.User_Data.objects.get(email=Reference.email)
         return HttpResponse("User Already Exists!!")
      except models.User_Data.DoesNotExist:
         try:
          Reference.OTP = obj.send_otp(Reference.email)
          print(Reference.OTP)
          if(Reference.OTP==1):
            return HttpResponse("Sorry, Unexpected Error has Occured!!")
          return render(request, 'OTP.html',{'email':Reference.email,'code':0})
         except Exception as e:
          print("::::Exception::::"+str(e))
          return HttpResponse("Sorry, Unexpected Error has Occured!!")
   else:
      return HttpResponse(":::Unauthorized Access is Denied:::")


# Signup Page
def Signup(request):
    if request.method == "POST":
        first_digit = request.POST.get('one')
        second_digit = request.POST.get('two')
        third_digit = request.POST.get('three')
        four_digit = request.POST.get('four')
        entered_otp = int(first_digit+second_digit+third_digit+four_digit)
        if(entered_otp==Reference.OTP):
         try:
          row = models.User_Data(username=Reference.username, password=Reference.password, email=Reference.email, phone=Reference.phone) 
          row.save()
          return render(request, 'OTP.html', {'email':Reference.email, 'code':1,'root_path':index.Root_path})
         except Exception as e :
           print(":::Exception:::"+str(e))
           return HttpResponse("Sorry, Unexpected Error has Occurred!! Please Try Again")
        else:
           return HttpResponse("Wrong OTP provided!!")
    else:
       return HttpResponse(":::Unauthorized Access is Denied:::")