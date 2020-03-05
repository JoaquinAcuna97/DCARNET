
from django.urls import include, path
from django.conf.urls import url,include
from autenticacion import views as aviews
from . import views


urlpatterns = [
    url(r'^autenticacion/',include('autenticacion.urls')),
    path('controlesmedicos/', views.controlesmedicos, name='Vercontroles'),
    path('agregarcontrol/', views.agregarcontrol, name='Agregarcontrol'),
]
