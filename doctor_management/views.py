from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import DoctorForm
from .models import Doctor


# =========================================================
# DOCTOR LIST
# =========================================================

@login_required
def doctor_list(request):

    search = request.GET.get(
        'search',
        ''
    ).strip()

    doctors = Doctor.objects.select_related(
        'user'
    ).order_by(
        'doctor_id'
    )

    if search:

        doctors = doctors.filter(
            Q(
                doctor_id__icontains=search
            )
            |
            Q(
                specialization__icontains=search
            )
            |
            Q(
                qualification__icontains=search
            )
        )

    paginator = Paginator(
        doctors,
        10
    )

    page_number = request.GET.get(
        'page'
    )

    doctors = paginator.get_page(
        page_number
    )

    # =====================================================
    # AJAX REQUEST
    # =====================================================

    if request.headers.get(
        'X-Requested-With'
    ) == 'XMLHttpRequest':

        return render(
            request,
            'doctors/partials/doctor_table.html',
            {
                'doctors': doctors,
                'search': search,
            }
        )

    # =====================================================
    # NORMAL REQUEST
    # =====================================================

    return render(
        request,
        'doctors/doctor_list.html',
        {
            'doctors': doctors,
            'search': search,
        }
    )


# =========================================================
# ADD DOCTOR
# =========================================================

@login_required
def doctor_create(request):

    if request.method == 'POST':

        form = DoctorForm(
            request.POST
        )

        if form.is_valid():

            form.save()

            return redirect(
                'doctor_list'
            )

    else:

        form = DoctorForm()

    return render(
        request,
        'doctors/doctor_form.html',
        {
            'form': form,
        }
    )


# =========================================================
# EDIT DOCTOR
# =========================================================

@login_required
def doctor_edit(
    request,
    doctor_id
):

    doctor = get_object_or_404(
        Doctor.objects.select_related(
            'user'
        ),
        id=doctor_id
    )

    # =====================================================
    # AJAX EDIT REQUEST
    # =====================================================

    if request.headers.get(
        'X-Requested-With'
    ) == 'XMLHttpRequest':

        # -------------------------------------------------
        # LOAD EDIT FORM
        # -------------------------------------------------

        if request.method == 'GET':

            form = DoctorForm(
                instance=doctor
            )

            return render(
                request,
                'doctors/partials/doctor_edit_form.html',
                {
                    'form': form,
                    'doctor': doctor,
                    'edit_mode': True,
                }
            )

        # -------------------------------------------------
        # SAVE EDIT FORM
        # -------------------------------------------------

        if request.method == 'POST':

            form = DoctorForm(
                request.POST,
                instance=doctor
            )

            if form.is_valid():

                form.save()

                return HttpResponse(
                    'success'
                )

            return render(
                request,
                'doctors/partials/doctor_edit_form.html',
                {
                    'form': form,
                    'doctor': doctor,
                    'edit_mode': True,
                }
            )

    # =====================================================
    # NORMAL EDIT REQUEST
    # =====================================================

    if request.method == 'POST':

        form = DoctorForm(
            request.POST,
            instance=doctor
        )

        if form.is_valid():

            form.save()

            return redirect(
                'doctor_list'
            )

    else:

        form = DoctorForm(
            instance=doctor
        )

    return render(
        request,
        'doctors/doctor_form.html',
        {
            'form': form,
            'edit_mode': True,
        }
    )


# =========================================================
# DELETE DOCTOR
# =========================================================

@login_required
def doctor_delete(
    request,
    doctor_id
):

    doctor = get_object_or_404(
        Doctor,
        id=doctor_id
    )

    # =====================================================
    # AJAX DELETE REQUEST
    # =====================================================

    if request.headers.get(
        'X-Requested-With'
    ) == 'XMLHttpRequest':

        # -------------------------------------------------
        # LOAD DELETE CONFIRMATION
        # -------------------------------------------------

        if request.method == 'GET':

            return render(
                request,
                'doctors/doctor_delete.html',
                {
                    'doctor': doctor,
                }
            )

        # -------------------------------------------------
        # CONFIRM DELETE
        # -------------------------------------------------

        if request.method == 'POST':

            doctor.delete()

            return HttpResponse(
                'success'
            )

    # =====================================================
    # NORMAL DELETE REQUEST
    # =====================================================

    if request.method == 'POST':

        doctor.delete()

        return redirect(
            'doctor_list'
        )

    return render(
        request,
        'doctors/doctor_delete.html',
        {
            'doctor': doctor,
        }
    )


# =========================================================
# DOCTOR PROFILE
# =========================================================

@login_required
def doctor_profile(
    request,
    doctor_id
):

    doctor = get_object_or_404(
        Doctor.objects.select_related(
            'user'
        ),
        id=doctor_id
    )

    return render(
        request,
        'doctors/doctor_profile.html',
        {
            'doctor': doctor,
        }
    )