from django.contrib import admin
from .models import Category, Tag, Post
from django_summernote.admin import SummernoteModelAdmin 


# Register your models here.
@admin.register(Category)
class CategoryAdmin(SummernoteModelAdmin):
    list_display = ('title', 'description','slug')


@admin.register(Tag)
class TagAdmin(SummernoteModelAdmin):
    list_display = ('title', 'tag_colour', 'tag_category_name')
    list_filter = ['tag_category__title', 'tag_colour']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('post_title', 'post_author', 'post_category', 'post_tag')
    list_filter = ['post_category', 'post_tag']