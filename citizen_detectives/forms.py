from django import forms
from .models import Category, Tag


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'description']


class TagForm(forms.ModelForm):
    disabled_fields = ('tag_category',)

    class Meta:
        model = Tag
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(TagForm, self).__init__(*args, **kwargs)
        for field in self.disabled_fields:
            self.fields[field].disabled = True

