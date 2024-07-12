from django.contrib import admin
from django.urls import path
from olcha import views

urlpatterns = [
    path('categories/', views.CategoryListView.as_view(), name='category_list'),
    path('category/<slug:slug>/', views.CategoryDetailView.as_view(), name='category_detail'),
]
