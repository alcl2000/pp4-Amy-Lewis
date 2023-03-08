from django import forms
from .models import Category, Tag


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'description']


class TagForm(forms.ModelFrom):
    class Meta:
        model = Tag
        fields = ['title', 'tag_colour']