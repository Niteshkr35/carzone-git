from django.shortcuts import render
#from . import views

# Create your views here.
def home(request):
    return render(request,'Pages/home.html')

def about(request):
    return render(request,'Pages/about.html')

def cars(request):
    return render(request,'Pages/cars.html')

def services(request):
    return render(request,'Pages/services.html')

def contact(request):
    return render(request,'Pages/contact.html')
