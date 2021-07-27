from django.urls import path
from . import views

app_name = 'paciente'

urlpatterns = [
    path('', views.index, name = 'index')
]