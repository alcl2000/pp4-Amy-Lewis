from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from django.views import generic, View
from citizen_detectives.models import Category
from citizen_detectives.forms import CategoryForm


# Create your views here.
class CategoryList(generic.ListView):
    model = Category
    queryset = Category.objects.order_by('-category_id')
    template_name = "category_list.html"
    # context = {
    #     'form': CategoryForm(),
    # }
    # post form to create new categories

 
def add_category(request):
    form = CategoryForm()
    context = {
        'form': form
    }
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/categories")
        else:
            form = CategoryForm()
    return render(request, 'add_category.html', context)

