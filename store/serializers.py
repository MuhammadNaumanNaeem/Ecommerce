from rest_framework import serializers
from .models import Category, Product 

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        read_only_fields = ("id", "created_at")


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source="category.name")
    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = ("id", "created_at")


