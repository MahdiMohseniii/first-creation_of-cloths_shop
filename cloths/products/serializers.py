from rest_framework import serializers
from .models import Product, Men, Women

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class MenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Men
        fields = '__all__'

class WomenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Women
        fields = '__all__'
        