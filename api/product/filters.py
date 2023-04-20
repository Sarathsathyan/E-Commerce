from django_filters import rest_framework as filters
from .models import Product

class ProductFilterSet(filters.FilterSet):
    category_id = filters.NumberFilter(field_name='sub_category__category__id')
    class Meta:
        model = Product
        fields = (
            'id','name','sub_category__id'
        )