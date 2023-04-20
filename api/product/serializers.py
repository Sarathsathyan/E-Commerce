from rest_framework import serializers
from .models import Product
from api.category.serializers import SubCategorySerializer

class ProductSerializer(serializers.ModelSerializer):
    sub_category_data = SubCategorySerializer(read_only=True, source='sub_category')
    class Meta:
        model = Product
        fields = ['id', 
                  'name', 
                  'description',
                  'price',
                  'sub_category', 
                  'sub_category_data']
        