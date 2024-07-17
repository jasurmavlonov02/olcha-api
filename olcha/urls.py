from django.contrib import admin
from django.urls import path
from olcha import views

urlpatterns = [
    path('categories/', views.CategoryListApiView.as_view(), name='category_list'),
    path('groups/', views.GroupListApiView.as_view(), name='group_list'),
    path('images/',views.ImageListApiView.as_view(), name='image_list'),
    path('products/', views.ProductListApiView.as_view(), name='products')
    # path('category/<slug:slug>/', views.CategoryDetailView.as_view(), name='category_detail'),
]
