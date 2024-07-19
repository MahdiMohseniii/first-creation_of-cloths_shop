from .models import Product, Men, Women
from .serializers import ProductSerializer, MenSerializer, WomenSerializer

from rest_framework import generics

class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class MenListCreate(generics.ListCreateAPIView):
    queryset = Men.objects.all()
    serializer_class = MenSerializer

class MenDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Men.objects.all()
    serializer_class = MenSerializer


class WomenListCreate(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer

class WomenDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer