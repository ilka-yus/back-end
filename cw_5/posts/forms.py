from django import forms
from .models import Thread, Post

class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['title']
        labels = {
            'title': 'Название',
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'picture', 'description']
        labels = {
            'title': 'Заголовок',
            'picture': 'Изображение',
            'description': 'Описание',
        }

    picture = forms.FileField(required=False)
    delete_picture = forms.BooleanField(required=False, initial=False)