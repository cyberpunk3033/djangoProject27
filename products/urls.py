from django.urls import path
from .views import products_view, create_product  #

urlpatterns = [
    path('products/', products_view, name='products'),

    path('create_product/', create_product, name='create_product'), # создание продукта
]