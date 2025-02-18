from django.db import models

class Thread(models.Model):
    name = models.CharField('Название', max_length=255)
    description = models.TextField('Описание')

    def __str__(self):
        return self.name
    

class Post(models.Model):
    title = models.CharField('Заголовок', max_length=255)
    picture = models.FileField('Изображение', upload_to='uploads/')
    description = models.TextField('Описание')
    author = models.CharField('Автор', max_length=255)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title