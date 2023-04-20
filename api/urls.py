from django.urls import path, include
from rest_framework_nested import routers

from api.category import views as category_views
from api.product import views as product_views

router = routers.SimpleRouter()

# category routes
router.register(r'categories', category_views.CategoryViewSet)
category_router = routers.NestedSimpleRouter(router, r'categories', lookup='category')
category_router.register(r'subcategories', category_views.SubCategoryViewSet, basename='sub-categories')

# product routes
router.register(r'products', product_views.ProductsViewSet)
product_router = routers.NestedSimpleRouter(router, r'products', lookup='product')

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(category_router.urls)),
    path(r'', include(product_router.urls))
]