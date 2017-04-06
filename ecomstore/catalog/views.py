from django.shortcuts import render, get_object_or_404
from .models import Category, Product


# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def category_list(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'category_list.html', context)

def category_detail(request, slug):
    category_object = get_object_or_404(Category, slug=slug)
    related_product = category_object.product_set.all()
    context = {
        'related_product': related_product
    }
    return render(request, 'category_detail.html', context)


def product_detail(request, slug):
    product_object = Product.objects.get(slug=slug)
    # product = product_object.categories.filter(is_active=True)
    context={
        'product': product_object,
    }
    return render(request, 'product_detail.html', context)