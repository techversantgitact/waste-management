from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

def index(request):
    context = {}
    return render(request, 'wasteapp/index.html', context)

def about(request):
    context = {}
    return render(request, 'wasteapp/about.html', context)
    

def contact(request):
    context = {}
    return render(request, 'wasteapp/contact.html', context)

def signin(request):
    context = {}
    return render(request, 'wasteapp/signin.html', context)

def signup(request):
    form = UserCreationForm()
    
    if request.method == "post":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
            
    context = {'form':form}
    return render(request, 'wasteapp/signup.html',context)
    
def logout(request):
    context = {}
    return render(request, 'wasteapp/logout.html', context)
    
    
