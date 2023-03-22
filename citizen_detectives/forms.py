from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Category, Tag, Post, Comment


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={
                                            'class': 'form-control'
                                            }),
            'description': forms.TextInput(attrs={
                                                  'class': 'form-control'
                                                  })
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['post_title', 'post_category', 'post_tag', 'post_content']
        widgets = {
                   'post_title': forms.TextInput(attrs={
                                                        'class': 'form-control'
                                                        }),
                   'post_category': forms.Select(attrs={
                                                        'class': 'form-select'
                                                        }),
                   'post_tag': forms.Select(attrs={
                                                        'class': 'form-select'
                                                        }),
                   'post_content': forms.Textarea(attrs={
                                                        'class': 'form-control'
                                                        })
                    }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text',]

        labels = {
            'text': _('add comment'),
        }
        
        widgets = {
            'text': forms.TextInput(),
        }