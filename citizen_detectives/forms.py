from django import forms
from bootstrap_modal_forms.form import BSModalModelForm
from .models import Category


class CategoryModalForm(BSModalModelForm):
    class Meta:
        model = Category
        fields = ['title', 'description']