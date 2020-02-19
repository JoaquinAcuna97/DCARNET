
from django.urls import include, path

from . import views

urlpatterns = [
    path('controlesmedicos/', views.controlesmedicos, name='Vercontroles'),
    path('', views.index, name='carnets'),
    path('agregarcontrol/', views.agregarcontrol, name='Agregarcontrol'),
]
