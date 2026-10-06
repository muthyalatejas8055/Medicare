from django.urls import path

from .views import (
    doctor_create,
    doctor_delete,
    doctor_edit,
    doctor_list,
    doctor_profile,
)


urlpatterns = [
    path(
        '',
        doctor_list,
        name='doctor_list'
    ),

    path(
        'add/',
        doctor_create,
        name='doctor_create'
    ),

    path(
        'edit/<int:doctor_id>/',
        doctor_edit,
        name='doctor_edit'
    ),

    path(
        'delete/<int:doctor_id>/',
        doctor_delete,
        name='doctor_delete'
    ),

    path(
        'profile/<int:doctor_id>/',
        doctor_profile,
        name='doctor_profile'
    ),
]