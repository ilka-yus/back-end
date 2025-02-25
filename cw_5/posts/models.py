from django.db import models
from django.contrib.auth.models import User

class Thread(models.Model):
    title = models.CharField('Название', max_length=255)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField('Заголовок', max_length=255)
    picture = models.FileField('Изображение', upload_to='uploads/')
    description = models.TextField('Описание')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='posts' )

    def __str__(self):
        return self.title