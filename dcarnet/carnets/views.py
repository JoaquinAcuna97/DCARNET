from django.shortcuts import render
from django.http import HttpResponse
from .models import Control

def index(request):
    return HttpResponse("Hello, world. You're at the App Carnets.")

def controlesmedicos(request):
    control= Control.objects.all()
    return render(request, 'carnets/icontrolmedico.html', {'control': control})

def agregarcontrol(request):
    return render(request, 'carnets/agregarcontrol.html')
