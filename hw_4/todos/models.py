from django.db import models

class TodoList(models.Model):
    title = models.CharField("Название", max_length=255)
    description = models.CharField("Описание", max_length=1000)

    def __str__(self):
        return self.title
    

class Todo(models.Model):
    title = models.CharField("Название", max_length=255)
    description = models.CharField("Описание", max_length=1000)
    due_date = models.DateField("Дата выполнения")
    status = models.BooleanField("Статус", default=False)
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE)

    def __str__(self):
        return self.title