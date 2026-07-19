from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from .services import *
from .analytics import *

from drf_spectacular.utils import extend_schema, extend_schema_view
from accounts.permissions import IsAdminOrReadOnly
from rest_framework.permissions import IsAuthenticated


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
    


class ProductStatisticsView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary="Product Statistics",
        description="Returns total products, average price, and total stock."
    )
    def get(self, request):
        try:
            return product_statistics()
        except Exception as e:
            return Response(
                {
                    "success": False,
                    "message": "Internal Server Error",
                    "error": str(e),
                },
                status=500,
            )


class CategoryStatisticsView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary="Category Statistics",
        description="Returns categories with the total number of products in each category."
    )
    def get(self, request):
        try:
            return category_statistics()
        except Exception as e:
            return Response(
                {
                    "success": False,
                    "message": "Internal Server Error",
                    "error": str(e),
                },
                status=500,
            )


class MonthlyProductStatisticsView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary="Monthly Product Statistics",
        description="Returns monthly product creation statistics."
    )
    def get(self, request):
        try:
            return monthly_product_statistics()
        except Exception as e:
            return Response(
                {
                    "success": False,
                    "message": "Internal Server Error",
                    "error": str(e),
                },
                status=500,
            )


class UserStatisticsView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary="User Statistics",
        description="Returns active users, inactive users, admin count, and normal user count."
    )
    def get(self, request):
        try:
            return user_statistics()
        except Exception as e:
            return Response(
                {
                    "success": False,
                    "message": "Internal Server Error",
                    "error": str(e),
                },
                status=500,
            )


class InventoryStatisticsView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary="Inventory Statistics",
        description="Returns total inventory value and average product price."
    )
    def get(self, request):
        try:
            return inventory_statistics()
        except Exception as e:
            return Response(
                {
                    "success": False,
                    "message": "Internal Server Error",
                    "error": str(e),
                },
                status=500,
            )