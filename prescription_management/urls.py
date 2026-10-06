from django.urls import path

from .views import (
    prescription_create,
    prescription_delete,
    prescription_edit,
    prescription_list,
)

urlpatterns = [
    path('', prescription_list, name='prescription_list'),
    path('add/', prescription_create, name='prescription_create'),
    path('edit/<int:prescription_id>/', prescription_edit, name='prescription_edit'),
    path('delete/<int:prescription_id>/', prescription_delete, name='prescription_delete'),
]