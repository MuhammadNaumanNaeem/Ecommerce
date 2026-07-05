from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


class CategoryView(APIView):
    def get(self, request):
        try:
            category = Category.objects.all()
            category_serializer = CategorySerializer(category, many=True)

            return Response({
                'success' : True,
                'message' : 'Data fetched Succesfully',
                'categories' : category_serializer.data
            }, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({
                'success' : False,
                'message' : 'Internal Server Error',
                'error' : str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def post(self, request):
        try:
            category = CategorySerializer(data=request.data)
            
            if category.is_valid():
                category.save()

                return Response({
                    'success' : True,
                    'message' : 'Category created Successfully',
                    'data' : category.data
                }, status=status.HTTP_201_CREATED)
            
            return Response({
                'success' : False,
                "message": "Validation Error",
                "errors": category.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({
                'success' : False,
                'message' : 'Internal Server Error',
                'error' : str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class CategoryDetailView(APIView):
    def get(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
            category_serializer = CategorySerializer(category)

            return Response({
                'success' : True,
                'message' : 'Data fetched Succesfully',
                'category' : category_serializer.data
            }, status=status.HTTP_200_OK)
        
        except Category.DoesNotExist:
            return Response({
                'success' : False,
                'message' : 'Category not found!'
            }, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({
                'success' : False,
                'message' : 'Internal Server Error',
                'error' : str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
            category_serializer = CategorySerializer(category, data=request.data)

            if category_serializer.is_valid():
                category_serializer.save()

                return Response({
                    'success' : True,
                    'message' : 'Data Updated Succesfully',
                    'category' : category_serializer.data
                }, status=status.HTTP_200_OK)
            
            return Response({
                    'success' : False,
                    'message' : 'validation Error',
                    'error' : category_serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)
        
        except Category.DoesNotExist:
            return Response({
                'success' : False,
                'message' : 'Category not found!'
            }, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({
                'success' : False,
                'message' : 'Internal Server Error',
                'error' : str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
            category_serializer = CategorySerializer(
                category,
                data=request.data,
                partial=True
            )

            if category_serializer.is_valid():
                category_serializer.save()

                return Response({
                    'success' : True,
                    "message": "Category Updated successfully",
                    "category": category_serializer.data
                }, status=status.HTTP_200_OK)

            return Response({
                'success' : False,
                "message": "Validation Error",
                "errors": category_serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        except Category.DoesNotExist:
            return Response({
                'success' : False,
                "message": "Category not found"
            }, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({
                'success' : False,
                "message": "Internal Server Error.",
                "error": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
            category.delete()

            return Response({
                'success' : True,
                "message": "Category Deleted successfully"
            }, status=status.HTTP_200_OK)

        except Category.DoesNotExist:
            return Response({
                'success' : False,
                "message": "Category not found"
            }, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({
                'success' : False,
                "message": "Internal Server Error",
                "error": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            


class ProductView(APIView):
    def get(self, request):
        try:
            product = Product.objects.all()
            product_serializer = ProductSerializer(product, many=True)

            return Response({
                'success' : True,
                'message' : 'Data fetched Succesfully',
                'products' : product_serializer.data
            }, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({
                'success' : False,
                'message' : 'Internal Server Error',
                'error' : str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def post(self, request):
        try:
            product = ProductSerializer(data=request.data)
            
            if product.is_valid():
                product.save()

                return Response({
                    'success' : True,
                    'message' : 'Product created Successfully',
                    'data' : product.data
                }, status=status.HTTP_201_CREATED)
            
            return Response({
                'success' : False,
                "message": "Validation Error",
                "errors": product.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({
                'success' : False,
                'message' : 'Internal Server Error',
                'error' : str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class ProductDetailView(APIView):
    def get(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
            product_serializer = ProductSerializer(product)

            return Response({
                'success' : True,
                'message' : 'Data fetched Succesfully',
                'product' : product_serializer.data
            }, status=status.HTTP_200_OK)
        
        except Product.DoesNotExist:
            return Response({
                'success' : False,
                'message' : 'Product not found!'
            }, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({
                'success' : False,
                'message' : 'Internal Server Error',
                'error' : str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
            product_serializer = ProductSerializer(product, data=request.data)

            if product_serializer.is_valid():
                product_serializer.save()

                return Response({
                    'success' : True,
                    'message' : 'Data Updated Succesfully',
                    'product' : product_serializer.data
                }, status=status.HTTP_200_OK)
            
            return Response({
                    'success' : False,
                    'message' : 'validation Error',
                    'error' : product_serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)
        
        except Product.DoesNotExist:
            return Response({
                'success' : False,
                'message' : 'Product not found!'
            }, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({
                'success' : False,
                'message' : 'Internal Server Error',
                'error' : str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
            product_serializer = ProductSerializer(
                product,
                data=request.data,
                partial=True
            )

            if product_serializer.is_valid():
                product_serializer.save()

                return Response({
                    'success' : True,
                    "message": "Product Updated successfully",
                    "product": product_serializer.data
                }, status=status.HTTP_200_OK)

            return Response({
                'success' : False,
                "message": "Validation Error",
                "errors": product_serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        except Product.DoesNotExist:
            return Response({
                'success' : False,
                "message": "Product not found"
            }, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({
                'success' : False,
                "message": "Internal Server Error.",
                "error": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
            product.delete()

            return Response({
                'success' : True,
                "message": "Product Deleted successfully"
            }, status=status.HTTP_200_OK)

        except Product.DoesNotExist:
            return Response({
                'success' : False,
                "message": "Product not found"
            }, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({
                'success' : False,
                "message": "Internal Server Error",
                "error": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            


