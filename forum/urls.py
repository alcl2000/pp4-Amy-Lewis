from . import views
from django.urls import path

urlpatterns = [
    path('categories/', views.CategoryList.as_view(), name='category_view'),
    path('add-category/', views.add_category, name='add_category'),
    path('category/<slug:slug>',
         views.CategoryDetailView.as_view(),
         name='category_detail'),
    path('delete/<category_id>',
         views.delete_category,
         name='delete_category'),
    path('edit/<category_id>', views.edit_category, name='edit_category'),
    path('add-tag/', views.add_tag, name='add_tag'),
    path('', views.IndexView.as_view(), name='home_page'),
    path('post/<slug:slug>', views.PostDetail.as_view(), name='post_detail'),
    path('post-delete/<slug:slug>', views.delete_post, name='post_delete'),
    path('post-edit/<slug:slug>', views.edit_post, name='post_edit'),
    path('comment-delete/<id>', views.delete_comment, name='delete_comment'),
    path('post-like/<slug:slug>', views.like_post, name='like_post')
]
