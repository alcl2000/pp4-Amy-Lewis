from django.contrib import admin
from .models import Category, Tag
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(Category)
class CategoryAdmin(SummernoteModelAdmin):
    list_display = ('title', 'description')


@admin.register(Tag)
class CategoryAdmin(SummernoteModelAdmin):
    list_display = ('title', 'tag_colour', 'tag_category_name')
    list_filter = ('tag_category', 'tag_colour')