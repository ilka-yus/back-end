from django import forms
from .models import Reservation
from tables.models import Table

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

    def clean_table(self):
        table = self.cleaned_data.get("table")
        if table and not table.is_available:
            raise forms.ValidationError("Этот столик недоступен для бронирования.")
        return table
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['table'].queryset = Table.objects.filter(is_available=True)