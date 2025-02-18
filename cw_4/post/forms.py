from django import forms
from .models import Thread, Post

class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['name', 'description']
        labels = {
            'name': 'Название',
            'description': 'Описание',
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'picture', 'description', 'author']
        labels = {
            'title': 'Заголовок',
            'picture': 'Изображение',
            'description': 'Описание',
            'author': 'Автор',
        }