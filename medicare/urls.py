from django.contrib import admin
from django.urls import include, path


from .views import (
    home,
    dashboard_upload_pdf,
    dashboard_upload_excel,
    dashboard_download_pdf,
    dashboard_download_excel,
    
)

from user_accounts.views import (
    login_view,
    logout_view,
    create_user,
)


urlpatterns = [

    # Administration
    path(
        'admin/',
        admin.site.urls
    ),

    # Dashboard
    path(
        '',
        home,
        name='home'
    ),

    # Authentication
    path(
        'login/',
        login_view,
        name='login'
    ),

    path(
        'logout/',
        logout_view,
        name='logout'
    ),

    # User management
    path(
        'users/create/',
        create_user,
        name='create_user'
    ),

    # Dashboard file management
    path(
        'dashboard/upload-pdf/',
        dashboard_upload_pdf,
        name='dashboard_upload_pdf'
    ),

    path(
        'dashboard/upload-excel/',
        dashboard_upload_excel,
        name='dashboard_upload_excel'
    ),

    path(
        'dashboard/download-pdf/',
        dashboard_download_pdf,
        name='dashboard_download_pdf'
    ),

    path(
        'dashboard/download-excel/',
        dashboard_download_excel,
        name='dashboard_download_excel'
    ),

    # Existing modules
    path(
        'patients/',
        include('patient_management.urls')
    ),

    path(
        'doctors/',
        include('doctor_management.urls')
    ),

    path(
        'appointments/',
        include('appointment_management.urls')
    ),



]