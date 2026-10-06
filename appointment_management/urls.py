from django.urls import path

from .views import (
    appointment_create,
    appointment_delete,
    appointment_edit,
    appointment_list,
)

urlpatterns = [
    path('', appointment_list, name='appointment_list'),

    path('add/', appointment_create, name='appointment_create'),

    path(
        'edit/<int:appointment_id>/',
        appointment_edit,
        name='appointment_edit'
    ),

    path(
        'delete/<int:appointment_id>/',
        appointment_delete,
        name='appointment_delete'
    ),
]