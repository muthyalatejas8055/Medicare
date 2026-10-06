from django.urls import path

from .views import (
    patient_create,
    patient_delete,
    patient_edit,
    patient_list,
    patient_upload_excel,
    patient_download_excel,
    patient_download_pdf,
)


urlpatterns = [

    path(
        '',
        patient_list,
        name='patient_list'
    ),

    path(
        'add/',
        patient_create,
        name='patient_create'
    ),

    path(
        'edit/<int:patient_id>/',
        patient_edit,
        name='patient_edit'
    ),

    path(
        'delete/<int:patient_id>/',
        patient_delete,
        name='patient_delete'
    ),

    path(
        'upload-excel/',
        patient_upload_excel,
        name='patient_upload_excel'
    ),

    path(
        'download-excel/',
        patient_download_excel,
        name='patient_download_excel'
    ),

    path(
        'download-pdf/<int:patient_id>/',
        patient_download_pdf,
        name='patient_download_pdf'
    ),
]