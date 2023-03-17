from django import forms
from .models import Category, Tag, Post


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'description']


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['post_title', 'post_category', 'post_tag', 'post_content']
