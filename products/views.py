from django.shortcuts import render
from .models import Product

from .forms import ProductForm
from django.http import HttpResponse

# Отображение продуктов
def products_view(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products.html', context)




# создание продукта
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProductForm()
    return render(request, 'create_product.html', {'form': form})