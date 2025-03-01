from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    due_date = forms.DateField(
        label='Дата выполнения',
        widget=forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        input_formats=['%Y-%m-%d']
    )

    class Meta:
        model = Todo
        fields = ['title', 'description', 'due_date', 'status']
        labels = {
            'title': 'Название',
            'description': 'Описание',
            'due_date': 'Дата выполнения',
            'status': 'Статус',
        }