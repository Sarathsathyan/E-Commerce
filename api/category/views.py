from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics, status, filters
from rest_framework.response import Response

from .models import Category, SubCategory

from .serializers import CategorySerializer, SubCategorySerializer

# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name','description']
    queryset = Category.objects.all()
   
    def list(self, request, pk=None):
        queryset = self.filter_queryset(self.queryset)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
   
class SubCategoryViewSet(generics.ListCreateAPIView, viewsets.ViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    filter_backends = [filters.SearchFilter]

    search_fields = ['name','description', 'category__name']

    def list(self, request, category_pk=None):
        queryset = self.queryset.filter(category_id = category_pk)
        queryset = self.filter_queryset(queryset)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk, *args, **kwargs):
        sub_category = get_object_or_404(SubCategory, pk=pk)
        sub_category_serializer = self.serializer_class(sub_category)
        return Response(sub_category_serializer.data, status=status.HTTP_200_OK)
        
    def destroy(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(SubCategory, pk=pk)
        instance.delete()
        return Response('Record deleted', status=status.HTTP_200_OK)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance= instance,
                                         data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)