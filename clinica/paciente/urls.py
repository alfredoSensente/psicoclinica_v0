from django.urls import path
from . import views

app_name = 'paciente'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('borrar_paciente/<int:pk>/', views.borrar_paciente, name='borrar'),
    path('nuevo_paciente/', views.nuevo_paciente, name='nuevo'),
]