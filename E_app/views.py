from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def new(request):
    return render(request, 'new.html')

def rain(request):
    return render(request, 'rain.html')

def snow(request):
    return render(request, 'snow.html')

def allweather(request):
    return render(request, 'allweather.html')
    
def shopall(request):
    return render(request, 'shopall.html')

def hub(request):
    return render(request, 'hub.html')

def signup(request):
    return render(request, 'signup.html')

def signin(request):
    return render(request, 'signin.html')