from django.shortcuts import render
from django.http import HttpResponse
from django.http import request
import time

# Create your views here.
APP_ID = "5089640493495656565"
def index(request):
    #params = 
    logged_in = False # look at using cookies?
    context = {
        'logged_in' : logged_in,
    }
    print("hello")
    return render(request, 'pindown/index.html', context)

def login(request):
    logged_in = True
    context = {
        "logged_in": True,
        "uname": request.POST['uname'],
    }
    return render(request, 'pindown/index.html', context)

