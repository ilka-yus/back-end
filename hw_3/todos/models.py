from django.db import models

class Todo(models.Model):
    title = models.CharField("Название", max_length=255)
    description = models.TextField("Описание")
    due_date = models.DateField("Дата выполнения")
    status = models.BooleanField("Статус", default=False)

    def __str__(self):
        return self.title