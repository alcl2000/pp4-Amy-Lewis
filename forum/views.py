from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
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

    # def add_category(request):
    #     if request.method == "POST":
    #         form = CategoryForm(request.POST)
    #         if form.is_valid():
    #             form.save()
    #             return HttpResponse(status=204)
    #     else:
    #         form = MovieForm()
    #     return render(request, 'category_list.html', {
    #         'form': form,
    #     })