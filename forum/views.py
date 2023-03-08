from django.shortcuts import (render, 
                              get_object_or_404, 
                              HttpResponseRedirect, 
                              redirect)
from django.views import generic, View
from django.contrib import messages
from citizen_detectives.models import Category, Post, Tag
from citizen_detectives.forms import CategoryForm


# Category CRUD functions/views
class CategoryList(generic.ListView):
    model = Category
    queryset = Category.objects.order_by('-category_id')
    template_name = "category_list.html"

 
def add_category(request):
    form = CategoryForm()
    context = {
        'form': form
    }
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category Added Successfully!')
            return redirect("/categories")
        else:
            form = CategoryForm()
    return render(request, 'add_category.html', context)


def delete_category(request, category_id):
    category = get_object_or_404(Category, category_id=category_id)
    category.delete()
    messages.success(request, 'Category Deleted Successfully!')
    return redirect("/categories")


def edit_category(request, category_id):
    category = get_object_or_404(Category, category_id=category_id)
    if request.method == POST:
        if request.method == 'POST':
            form = CategoryForm(request.POST, instance=category)
            if form.is_valid():
                form.save()
                return redirect('get_todo_list')
    form = CategoryForm(instance=item)
    context = {
        "form": form
    }
    return render(request, 'todo/edit_todo.html', context)


class CategoryDetailView(View):
    def get(self, request, slug, *args, **kwargs):
        category = get_object_or_404(Category, slug=slug)
        category_id = int(category.category_id)
        posts = Post.objects.filter(
                                    post_category=category_id
                                    ).order_by('-post_date')
        tags = Tag.objects.filter(tag_category=category_id)
        return render(request, 'category_detail.html',
                      {
                        'category': category,
                        'posts': posts,
                        'tags': tags
                      })
