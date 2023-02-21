from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Category


# Create your views here.
class CategoryList(View):
    model = Post
    queryset = Post.objects.order_by('-category_id')
    template_name = "category-list.html"