from django.urls import path
from .views import ProductListCreateView, ProductDetailView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<slug:slug>/', ProductDetailView.as_view(), name='product-detail'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)