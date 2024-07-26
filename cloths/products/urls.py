from django.conf import settings  
from django.conf.urls.static import static  
from django.urls import path
from . import views 
from .views import (
    ProductListCreate, ProductDetail,
    MenListCreate, MenDetail,
    WomenListCreate, WomenDetail
)

# these urls refers to API_VIEW
urlpatterns = [
    path('products/', ProductListCreate.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),

    path('men/', MenListCreate.as_view(), name='men-list-create'),
    path('men/<int:pk>/', MenDetail.as_view(), name='men-detail'),

    path('women/', WomenListCreate.as_view(), name='woman-list-create'),
    path('women/<int:pk>/', WomenDetail.as_view(), name='woman-detail'),
]
if settings.DEBUG:
   urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# these urls refers to templates_View

urlpatterns = [  
    path('men/', views.MenListView.as_view(), name='men-list'),  
    path('men/add/', views.MenCreateView.as_view(), name='men-add'),  
    path('men/<int:pk>/edit/', views.MenUpdateView.as_view(), name='men-edit'),  
    path('men/<int:pk>/delete/', views.MenDeleteView.as_view(), name='men-delete'),  
    path('women/', views.WomenListView.as_view(), name='women-list'),  
    path('women/add/', views.WomenCreateView.as_view(), name='women-add'),  
    path('women/<int:pk>/edit/', views.WomenUpdateView.as_view(), name='women-edit'),  
    path('women/<int:pk>/delete/', views.WomenDeleteView.as_view(), name='women-delete'),  
]  
