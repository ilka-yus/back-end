from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    title = models.CharField('Название', max_length=255)
    description = models.CharField('Описание', max_length=1000)
    due_date = models.DateField('Дата выполнения')
    status = models.BooleanField('Статус', default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title