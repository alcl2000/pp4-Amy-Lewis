from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views import generic, View
from citizen_detectives.models import Category
from citizen_detectives.forms import CategoryForm


# Create your views here.
class CategoryList(generic.ListView):
    model = Category
    queryset = Category.objects.order_by('-category_id')
    template_name = "category_list.html"
    # post form to create new categories

    def get_context_data(self, **kwargs):
        context = super(CategoryList, self).get_context_data(**kwargs)
        context['form'] = CategoryForm()
        return context
        return HttpResponseRedirect('/categories/')