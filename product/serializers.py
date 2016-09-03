from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('name', 'barcode', 'category', 'quantity', 'price', 'description', 'get_rating')

    def get_category(self, obj):
        return obj.category.name

