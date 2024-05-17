from django.shortcuts import render
from django.http import HttpResponse
# Home Page
def returnHomePage(request):
    if request.session["isAuthenticated"]==False:
        return HttpResponse("PERMISSION DENIED -- LOGIN FIRST!")
    return render(request,'Test.html',{'Value':"Home Page"})
