from . import views
from django.urls import path

urlpatterns = [
    path('categories/', views.CategoryList.as_view(), name='category_view'),
    path('add-category/', views.add_category, name='add_category'),
    path('category/<slug:slug>', 
         views.CategoryDetailView.as_view(), 
         name='category_detail'),
    path('delete/<category_id>', views.delete_category, name='delete_category')
]
