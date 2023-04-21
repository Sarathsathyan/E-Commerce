from rest_framework import serializers
from .models import Category, SubCategory

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description')


class SubCategorySerializer(serializers.ModelSerializer):

    category_data = CategorySerializer(read_only=True, source='category')
    
    class Meta:
        model = SubCategory
        fields = ('id', 'name', 'description','category_data','category')   