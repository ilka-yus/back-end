from django.shortcuts import render, redirect, get_object_or_404
from .models import Table
from .forms import TableForm
from reservations.models import Reservation
from django.utils.dateparse import parse_date

def table_list(request):
    tables = Table.objects.all()
    return render(request, 'tables/list.html', {'tables': tables})

def table_create(request):
    if request.method == 'POST':
        form = TableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('table_list')
    else:
        form = TableForm()
    return render(request, 'tables/create.html', {'form': form})

def table_available(request):
    date_str = request.GET.get('date')
    available_tables = Table.objects.filter(is_available=True)

    if date_str:
        date = parse_date(date_str)
        if date:
            reserved_tables = Reservation.objects.filter(date=date).values_list('table_id', flat=True)
            available_tables = available_tables.exclude(id__in=reserved_tables)

    return render(request, 'tables/available.html', {'tables': available_tables, 'date': date_str})

def table_detail(request, id):
    table = get_object_or_404(Table, id=id)
    return render(request, 'tables/detail.html', {'table': table})

def table_update(request, id):
    table = get_object_or_404(Table, id=id)

    if request.method == 'POST':
        form = TableForm(request.POST, instance=table)
        if form.is_valid():
            form.save()
            return redirect('table_detail', id=id)
    else:
        form = TableForm(instance=table)

    return render(request, 'tables/update.html', {'form': form, 'table': table})