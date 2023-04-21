from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics, status, filters
from rest_framework.response import Response

# import models
from .models import Category, SubCategory
# import serializers
from .serializers import CategorySerializer, SubCategorySerializer

# Create views here.
class CategoryViewSet(viewsets.ModelViewSet):
    """
        Viewset for Category
        ModelViewSet can handle all CRUD Operations
        serializer : CategorySerializer
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name','description']
   
    def list(self, request, pk=None):
        # List Categories based on params
        queryset = self.filter_queryset(self.queryset)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
   
class SubCategoryViewSet(generics.ListCreateAPIView, viewsets.ViewSet):
    """
        ViewSet for create and list all Sub categories

    """
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description', 'category__name']

    def list(self, request, category_pk=None):
        queryset = self.queryset.filter(category_id = category_pk)
        queryset = self.filter_queryset(queryset)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk, *args, **kwargs):
        # Retrive a subcategory
        sub_category = get_object_or_404(SubCategory, pk=pk)
        sub_category_serializer = self.serializer_class(sub_category)
        return Response(sub_category_serializer.data, status=status.HTTP_200_OK)
        
    def destroy(self, request, pk, *args, **kwargs):
        # Delete sub category
        instance = get_object_or_404(SubCategory, pk=pk)
        instance.delete()
        return Response('Record deleted', status=status.HTTP_200_OK)
    
    def update(self, request, *args, **kwargs):
        # Update Sub Category
        instance = self.get_object()
        serializer = self.get_serializer(instance= instance,
                                         data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)