"""Urls Paciente"""
from django.urls import path
from . import views

app_name = 'paciente'

urlpatterns = [
    path(
        '',
        views.index,
        name = 'index'
    ),
    path(
        'nuevo_paciente/',
        views.nuevo_paciente,
        name='nuevo'
    ),
    path(
        'editar_paciente/<int:id_paciente>/',
        views.editar_paciente,
        name='editar'
    ),
    path(
        'borrar_paciente/<int:id_paciente>/',
        views.borrar_paciente,
        name='borrar'
    ),
    path(
        'detalle_paciente/<int:id_paciente>/',
        views.detalle_paciente,
        name='detalle'
    ),
    path(
        'detalle_paciente/<int:id_paciente>/nuevo_contacto/',
        views.ContactoCreate.as_view(),
        name='nuevo_contacto'
    ),
    path(
        'detalle_paciente/<int:id_paciente>/editar_contacto/<int:id_contacto>/',
        views.ContactoUpdate.as_view(),
        name='nuevo_contacto'
    ),
]
