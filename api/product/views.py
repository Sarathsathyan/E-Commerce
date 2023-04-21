from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics, status, filters
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer
from .filters import ProductFilterSet
# Create your views here.

class ProductsViewSet(viewsets.ModelViewSet):
    """
        Products listing and create viewset
        serializer : ProductSerializer
        
    """
    serializer_class = ProductSerializer
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter)
    search_fields = ['name','description']
    filterset_class = ProductFilterSet
    queryset = Product.objects.all()


    def list(self, request, pk=None):
        queryset = self.filter_queryset(self.get_queryset())
        # Setting up pagination
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    

    def get_queryset(self):
        query_params = self.request.query_params
        if 'price' in query_params.keys():
            min, max = query_params.get('price').split(',')
            if min != u'None':
                self.queryset = self.queryset.filter(price__gte=min)
            if max != u'None':
                self.queryset = self.queryset.filter(price__lte=max)
        return self.queryset


