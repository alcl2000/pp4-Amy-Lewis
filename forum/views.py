from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from citizen_detectives.models import Category
from citizen_detectives.forms import CategoryForm


# Create your views here.
class CategoryList(generic.ListView):
    model = Category
    queryset = Category.objects.order_by('-category_id')
    template_name = "category_list.html"
    # post form to create new categories