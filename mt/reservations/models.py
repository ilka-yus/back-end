from django.db import models
from django.contrib.auth.models import User
from customers.models import Customer
from tables.models import Table

class Reservation(models.Model):
    STATUS_CHOICES = [
        ('pending', 'В ожидании'),
        ('confirmed', 'Подтвержден'),
        ('canceled', 'Отклонен'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f'Бронь для {self.customer.name} на {self.date}'