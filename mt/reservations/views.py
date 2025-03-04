from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Reservation
from .forms import ReservationForm
from customers.models import Customer
from tables.models import Table

def reservation_list(request):
    reservations = Reservation.objects.all()
    return render(request, 'reservations/list.html', {'reservations': reservations})

def reservation_create(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            customer = form.cleaned_data['customer']
            table = form.cleaned_data['table']
            date = form.cleaned_data['date']

            if Reservation.objects.filter(customer=customer, date=date).exists():
                return HttpResponse('У Вас уже есть бронь на этот день.', status=400)
        
            if Reservation.objects.filter(table=table, date=date).exists():
                return HttpResponse('Этот столик уже забронирован на эту дату', status=400)

            if not table.is_available:
                form.add_error('table', 'Выбранный стол недоступен для бронирования')
            else:
                form.save()
                return redirect('reservation_list')
    
    else:
        form = ReservationForm()

    return render(request, 'reservations/create.html', {'form': form})

def reservation_detail(request, id):
    reservation = get_object_or_404(Reservation, id=id)
    return render(request, 'reservations/detail.html', {'reservation': reservation})

def reservation_list_by_user(request, user_id):
    customer = get_object_or_404(Customer, id=user_id)
    reservations = Reservation.objects.filter(customer=customer)
    return render(request, "reservations/user_reservations.html", {"customer": customer, "reservations": reservations})

def reservation_update(request, id):
    reservation = get_object_or_404(Reservation, id=id)

    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('reservation_detail', id=id)
    else:
        form = ReservationForm(instance=reservation)

    return render(request, 'reservations/update.html', {'form': form, 'reservation': reservation})
        
def reservation_delete(request, id):
    reservation = get_object_or_404(Reservation, id=id)
    if request.method == 'POST':
        reservation.delete()
        return redirect('reservation_list')
    return render(request, 'reservations/delete.html', {'reservation': reservation})