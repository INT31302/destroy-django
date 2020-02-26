from django import forms
from .models import Post, Comment
from django.conf import settings


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        labels = {
            'title': '제목',
            'content': '내용',
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control'
            })
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', ]
        labels = {
            "text": "댓글"
        }
        widgets = {
            "text": forms.Textarea(attrs={
                'placeholder': '댓글을 입력해주세요',
                'class': 'form-control', 'rows': 5}),
        }
