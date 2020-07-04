from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    description = forms.CharField()

    class Meta:
        model = Post
        fields = '__all__'


class CommentForm(forms.ModelForm):
    content = forms.Textarea(attrs={'class': 'form-control'})

    class Meta:
        model = Comment
        fields = ('content',)
