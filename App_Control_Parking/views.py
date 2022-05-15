from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the App_Control_Parking index.")

