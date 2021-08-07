from django.urls import path
from . import views

app_name = 'paciente'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('nuevo_paciente/', views.nuevo_paciente, name='nuevo'),
    path('editar_paciente/<int:pk>/', views.editar_paciente, name='editar'),
    path('borrar_paciente/<int:pk>/', views.borrar_paciente, name='borrar'),
]