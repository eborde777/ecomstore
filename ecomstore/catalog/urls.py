from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

app_name = 'catalog'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^catalog_list/$', views.category_list, name = 'category_list'),
    url(r'^category/(?P<slug>[-\w]+)/$', views.category_detail, name='category'),
    url(r'^product/(?P<slug>[-\w]+)/$', views.product_detail, name='product'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)