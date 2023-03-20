from django.shortcuts import (render, 
                              get_object_or_404, 
                              HttpResponseRedirect, 
                              redirect)
from django.views import generic, View
from django.contrib import messages
from citizen_detectives.models import Category, Post, Tag, Comment
from citizen_detectives.forms import (CategoryForm, 
                                      TagForm, 
                                      PostForm, 
                                      CommentForm)


# Category CRUD functions/views
class CategoryList(generic.ListView):
    model = Category
    queryset = Category.objects.order_by('-category_id')
    template_name = "category_list.html"

 
def add_category(request):
    form = CategoryForm()
    title_and_text = "Add Category"
    context = {
        'form': form,
        "title_and_text": title_and_text
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
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('/categories')
    form = CategoryForm(instance=category)
    title_and_text = "Edit Category"
    context = {
        "form": form,
        "title_and_text": title_and_text
    }
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

# Tag CRUD functions/views


def add_tag(request, category_id):
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tag Added Successfully!')
            return redirect("/categories")
        else:
            form = TagForm()
    form = TagForm(initial={'tag_category': category_id})
    title_and_text = 'Add Tag'
    category_id = category_id
    category = get_object_or_404(Category, category_id=category_id)
    category_title = category.title
    context = {
        'form': form,
        'title_and_text': title_and_text,
        'category_title': category_title
        }
    return render(request, 'add_tag.html', context)

# Index view


class IndexView(View):

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        queryset = Post.objects.order_by('-post_id')
        categories = Category.objects.all()
        context = {
                   'form': PostForm,
                   'posts': posts,
                   'categories': categories}
        return render(request, "index.html", context) 

    def post(self, request, *args, **kwargs):
        posts = Post.objects.all()
        queryset = Post.objects.order_by('-post_id')
        context = {
                    'form': PostForm,
                    'posts': posts
                }
        if request.method == 'POST':
            form = PostForm(data=request.POST)
            if form.is_valid:
                post = form.save(commit=False)
                post.post_author = request.user
                form.save()
                return redirect('home_page')
        else:
            form = PostForm()
        return render(request, 'index.html', context) 

# post detail view


class PostDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, slug=slug)
        comments = Comment.objects.filter(post=post)
        context = {'post': post, 
                   'form': CommentForm,
                   'comments': comments
                   }
        context = {'post': post, 'form': CommentForm}
        return render(request, 'post_detail.html', context)

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, slug=slug)
        comments = Comment.objects.filter(post=post)
        context = {'post': post, 
                   'form': CommentForm,
                   'comments': comments
                   }
        if request.method == 'POST':
            form = CommentForm(data=request.POST)
            if form.is_valid:
                comment = form.save(commit=False)
                comment.comment_author = request.user
                comment.post = post
                form.save()
                return render(request, 'post_detail.html', context)

# post edit/ delete


def delete_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    messages.success(request, 'Post deleted sucessfully')
    return redirect('home_page')


def edit_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    slug = slug
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save(commit=False)
            post.post_author = request.user
            form.save()
            messages.success(request, 'Post edited successfully!')
            return redirect('post_detail', slug=slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})


def delete_comment(request, id):
    comment = get_object_or_404(Comment, id=id)
    comment.delete()
    return redirect(request.META.get('HTTP_REFERER'))