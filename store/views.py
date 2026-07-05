from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from .services import *


class CategoryView(APIView):
    def get(self, request):
        return get_categories()

    def post(self, request):
        return create_category(request)

class CategoryDetailView(APIView):

    def get(self, request, pk):
        return get_category(pk)

    def put(self, request, pk):
        return update_category(request, pk)

    def patch(self, request, pk):
        return partial_update_category(request, pk)

    def delete(self, request, pk):
        return delete_category(pk)


class ProductView(APIView):
    def get(self, request):
        return get_products()

    def post(self, request):
        return create_product(request)

class ProductDetailView(APIView):

    def get(self, request, pk):
        return get_product(pk)

    def put(self, request, pk):
        return update_product(request, pk)

    def patch(self, request, pk):
        return partial_update_product(request, pk)

    def delete(self, request, pk):
        return delete_product(pk)