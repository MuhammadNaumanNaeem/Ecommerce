from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from .services import *

from drf_spectacular.utils import extend_schema, extend_schema_view
from accounts.permissions import IsAdminOrReadOnly


@extend_schema_view(
    get=extend_schema(summary="Get Categories"),
    post=extend_schema(summary="Create Category"),
)
class CategoryView(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request):
        return get_categories()

    def post(self, request):
        return create_category(request)


@extend_schema_view(
    get=extend_schema(summary="Get Category"),
    put=extend_schema(summary="Update Category"),
    patch=extend_schema(summary="Partial Update Category"),
    delete=extend_schema(summary="Delete Category"),
)
class CategoryDetailView(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request, pk):
        return get_category(pk)

    def put(self, request, pk):
        return update_category(request, pk)

    def patch(self, request, pk):
        return partial_update_category(request, pk)

    def delete(self, request, pk):
        return delete_category(pk)



@extend_schema_view(
    get=extend_schema(summary="Get Product"),
    post=extend_schema(summary="Create Product"),
)
class ProductView(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request):
        return get_products()

    def post(self, request):
        return create_product(request)


@extend_schema_view(
    get=extend_schema(summary="Get Product"),
    put=extend_schema(summary="Update Product"),
    patch=extend_schema(summary="Partial Update Product"),
    delete=extend_schema(summary="Delete Product"),
)
class ProductDetailView(APIView):
    permission_classes = [IsAdminOrReadOnly]
    
    def get(self, request, pk):
        return get_product(pk)

    def put(self, request, pk):
        return update_product(request, pk)

    def patch(self, request, pk):
        return partial_update_product(request, pk)

    def delete(self, request, pk):
        return delete_product(pk)