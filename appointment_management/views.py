from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator

from .forms import AppointmentForm
from .models import Appointment


@login_required
def appointment_list(request):
    appointments = Appointment.objects.select_related(
        'patient',
        'doctor'
    ).order_by(
        '-appointment_date',
        '-appointment_time'
    )

    paginator = Paginator(appointments, 10)
    page_number = request.GET.get('page')
    appointments = paginator.get_page(page_number)

    return render(
        request,
        'appointments/appointment_list.html',
        {'appointments': appointments}
    )

@login_required
def appointment_create(request):

    if request.method == 'POST':
        form = AppointmentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('appointment_list')

    else:
        form = AppointmentForm()

    return render(
        request,
        'appointments/appointment_form.html',
        {'form': form}
    )


@login_required
def appointment_edit(request, appointment_id):

    appointment = get_object_or_404(
        Appointment,
        id=appointment_id
    )

    if request.method == 'POST':
        form = AppointmentForm(
            request.POST,
            instance=appointment
        )

        if form.is_valid():
            form.save()
            return redirect('appointment_list')

    else:
        form = AppointmentForm(
            instance=appointment
        )

    return render(
        request,
        'appointments/appointment_form.html',
        {
            'form': form,
            'edit_mode': True
        }
    )


@login_required
def appointment_delete(request, appointment_id):

    appointment = get_object_or_404(
        Appointment,
        id=appointment_id
    )

    if request.method == 'POST':
        appointment.delete()
        return redirect('appointment_list')

    return render(
        request,
        'appointments/appointment_delete.html',
        {'appointment': appointment}
    )