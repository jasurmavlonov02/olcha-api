from django.contrib import admin
from django.urls import path, include
from olcha import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('categories', views.CategoryModelViewSet, basename='category')

urlpatterns = [
    path('categories/', views.CategoryListApiView.as_view(), name='category_list'),
    path('groups/', views.GroupListApiView.as_view(), name='group_list'),
    path('images/', views.ImageListApiView.as_view(), name='image_list'),
    path('products/', views.ProductListApiView.as_view(), name='products'),

    # path('category/<slug:slug>/', views.CategoryDetailView.as_view(), name='category_detail'),
    path('category-list-generic-api-view/', views.CategoryList.as_view(), name='category_list_generic'),
    path('category-detail-generic-api-view/<int:pk>', views.CategoryDetail.as_view()),
    path('category-add-generic-api-view/', views.CategoryAdd.as_view()),
    path('category-change-generic-api-view/<int:pk>', views.CategoryChange.as_view()),
    path('category-delete-generic-api-view/<int:pk>', views.CategoryDelete.as_view()),
    path('modelviewset/', include(router.urls))
]
