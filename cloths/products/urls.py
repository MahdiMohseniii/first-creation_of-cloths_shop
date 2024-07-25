from django.conf import settings  
from django.conf.urls.static import static  
from django.urls import path
from .views import (
    ProductListCreate, ProductDetail,
    MenListCreate, MenDetail,
    WomenListCreate, WomenDetail
)


urlpatterns = [
    path('products/', ProductListCreate.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),

    path('men/', MenListCreate.as_view(), name='men-list-create'),
    path('men/<int:pk>/', MenDetail.as_view(), name='men-detail'),

    path('women/', WomenListCreate.as_view(), name='woman-list-create'),
    path('women/<int:pk>/', WomenDetail.as_view(), name='woman-detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)