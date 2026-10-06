from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PrescriptionForm
from .models import Prescription



@login_required
def prescription_list(request):

    prescriptions = Prescription.objects.select_related(
        'patient',
        'doctor'
    ).order_by(
        '-prescribed_date'
    )

    return render(
        request,
        'prescriptions/prescription_list.html',
        {
            'prescriptions': prescriptions
        }
    )


@login_required
def prescription_create(request):

    if request.method == 'POST':

        form = PrescriptionForm(
            request.POST
        )

        if form.is_valid():

            form.save()

            return redirect(
                'prescription_list'
            )

    else:

        form = PrescriptionForm()

    return render(
        request,
        'prescriptions/prescription_form.html',
        {
            'form': form
        }
    )


@login_required
def prescription_edit(request, prescription_id):

    prescription = get_object_or_404(
        Prescription,
        id=prescription_id
    )

    if request.method == 'POST':

        form = PrescriptionForm(
            request.POST,
            instance=prescription
        )

        if form.is_valid():

            form.save()

            return redirect(
                'prescription_list'
            )

    else:

        form = PrescriptionForm(
            instance=prescription
        )

    return render(
        request,
        'prescriptions/prescription_form.html',
        {
            'form': form,
            'edit_mode': True
        }
    )


@login_required
def prescription_delete(request, prescription_id):

    prescription = get_object_or_404(
        Prescription,
        id=prescription_id
    )

    if request.method == 'POST':

        prescription.delete()

        return redirect(
            'prescription_list'
        )

    return render(
        request,
        'prescriptions/prescription_delete.html',
        {
            'prescription': prescription
        }
    )