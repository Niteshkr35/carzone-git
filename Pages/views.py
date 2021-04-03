from django.shortcuts import render
from .models import Team

# Create your views here.
def home(request):
    teams = Team.objects.all()
    data = {
        'teams':teams,
    }
    return render(request,'Pages/home.html',data)

def about(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request,'Pages/about.html',data)

def cars(request):
    return render(request,'Pages/cars.html')

def services(request):
    return render(request,'Pages/services.html')

def contact(request):
    return render(request,'Pages/contact.html')
