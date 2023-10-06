from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.product_create, name='product_create'),
    path('posts/<int:post_id>/edit/', views.product_edit, name='product_edit'),
] 