from django.shortcuts import render
from django.http import HttpResponse
from . import models

    #update and create views

def controlesmedicos(request):
    #control= Control.objects.all()
    #return render(request, 'carnets/icontrolmedico.html', {'control': control})
    return render(request, 'carnets/agregarcontrol.html')

def agregarcontrol(request):

    return render(request, 'carnets/agregarcontrol.html')
