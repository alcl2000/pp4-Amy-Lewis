from . import views
from django.urls import path

urlpatterns = [
    path('categories/', views.CategoryList.as_view(), name='category_view'),
    path('add-category/', views.add_category, name='add_category')
]