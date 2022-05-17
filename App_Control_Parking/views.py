from django.shortcuts import HttpResponse
from django.shortcuts import render, redirect

# Models
from App_Control_Parking.models import Usuario


def index(request):
    return render(request, 'index.html')
   
def register(request):
    return render(request, 'register.html')
    
def consult(request):
    context = Usuario.objects.all()
    print("Contest: ", context)
    return render(request, 'consult.html', {'context': context})

def register_user(request):
    return render(request, 'register_user.html')
    
