from django.contrib import admin
from django.urls import path
from olcha import views

urlpatterns = [
    path('categories/', views.CategoryListApiView.as_view(), name='category_list'),
    path('groups/',views.GruopListApiView.as_view(), name='group_list')
    # path('category/<slug:slug>/', views.CategoryDetailView.as_view(), name='category_detail'),
]
