from django.shortcuts import (render, 
                              get_object_or_404, 
                              HttpResponseRedirect, 
                              redirect)
from django.views import generic, View
from citizen_detectives.models import Category, Post, Tag
from citizen_detectives.forms import CategoryForm


# Create your views here.
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
            return redirect("/categories")
        else:
            form = CategoryForm()
    return render(request, 'add_category.html', context)


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
