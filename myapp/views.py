from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
#def home(request):
# return HttpResponse("Hello World")

def home(request):
 return render(request,'home.html')


def aboutus(request):
 return render(request, "aboutus.html")

def contactus(request):
 return render(request, "contactus.html")
