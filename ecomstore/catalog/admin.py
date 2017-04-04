from django.contrib import admin
from .models import Category, Product
from .forms import ProductAdminForm

# Register your models here.
class CategoryModelAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display = ['name', 'created_at', 'updated_at']
    list_display_links = ['name']
    search_fields = ['name', 'slug']

    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryModelAdmin)

class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'old_price','created_at', 'updated_at']
    list_display_links = ['name']
    search_fields = ['name', 'slug']

    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Product, ProductModelAdmin)
