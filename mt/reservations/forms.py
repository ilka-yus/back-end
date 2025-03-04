from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['customer', 'table', 'date', 'status']
        labels = {
            'customer': 'Имя',
            'table': 'Cтол',
            'date': 'Дата',
            'status': 'Статус',
        }
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }