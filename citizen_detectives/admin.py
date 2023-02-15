from django.contrib import admin
from .models import Category
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(Category)
class CategoryAdmin(SummernoteModelAdmin):
    list_display = ('title',)