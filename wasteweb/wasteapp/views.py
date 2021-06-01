from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
#from django.http import HttpResponse


def index(request):
    context = {}
    return render(request, 'wasteapp/index.html', context)

def about(request):
    context = {}
    return render(request, 'wasteapp/about.html', context)
    

def contact(request):
    context = {}
    return render(request, 'wasteapp/contact.html', context)

def login(request):
    context = {}
    return render(request, 'wasteapp/signin.html', context)

def signup(request):
    context = {}
    return render(request, 'wasteapp/signup.html',context)
    
def logout(request):
    context = {}
    return render(request, 'wasteapp/logout.html', context)
    
    
