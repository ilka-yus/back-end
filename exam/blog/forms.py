from django import forms
from ...sessia.blog.models import Post, Comment
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']