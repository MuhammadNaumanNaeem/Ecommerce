from rest_framework.response import Response
from rest_framework import status

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


# Category

def get_categories():
    try:
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)

        return Response({
            "success": True,
            "message": "Data fetched successfully",
            "categories": serializer.data
        }, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({
            "success": False,
            "message": "Internal Server Error",
            "error": str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def create_category(request):
    try:
        serializer = CategorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({
                "success": True,
                "message": "Category created successfully",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)

        return Response({
            "success": False,
            "message": "Validation Error",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({
            "success": False,
            "message": "Internal Server Error",
            "error": str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def get_category(pk):
    try:
        category = Category.objects.get(pk=pk)
        serializer = CategorySerializer(category)

        return Response({
            "success": True,
            "message": "Data fetched successfully",
            "category": serializer.data
        }, status=status.HTTP_200_OK)

    except Category.DoesNotExist:
        return Response({
            "success": False,
            "message": "Category not found!"
        }, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        return Response({
            "success": False,
            "message": "Internal Server Error",
            "error": str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def update_category(request, pk):
    try:
        category = Category.objects.get(pk=pk)
        serializer = CategorySerializer(category, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({
                "success": True,
                "message": "Category updated successfully",
                "category": serializer.data
            }, status=status.HTTP_200_OK)

        return Response({
            "success": False,
            "message": "Validation Error",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    except Category.DoesNotExist:
        return Response({
            "success": False,
            "message": "Category not found!"
        }, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        return Response({
            "success": False,
            "message": "Internal Server Error",
            "error": str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def partial_update_category(request, pk):
    try:
        category = Category.objects.get(pk=pk)
        serializer = CategorySerializer(
            category,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()

            return Response({
                "success": True,
                "message": "Category updated successfully",
                "category": serializer.data
            }, status=status.HTTP_200_OK)

        return Response({
            "success": False,
            "message": "Validation Error",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    except Category.DoesNotExist:
        return Response({
            "success": False,
            "message": "Category not found!"
        }, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        return Response({
            "success": False,
            "message": "Internal Server Error",
            "error": str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def delete_category(pk):
    try:
        category = Category.objects.get(pk=pk)
        category.delete()

        return Response({
            "success": True,
            "message": "Category deleted successfully"
        }, status=status.HTTP_200_OK)

    except Category.DoesNotExist:
        return Response({
            "success": False,
            "message": "Category not found!"
        }, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        return Response({
            "success": False,
            "message": "Internal Server Error",
            "error": str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



#Product 

def get_products():
    try:
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)

        return Response({
            "success": True,
            "message": "Data fetched successfully",
            "products": serializer.data
        }, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({
            "success": False,
            "message": "Internal Server Error",
            "error": str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def create_product(request):
    try:
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({
                "success": True,
                "message": "Product created successfully",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)

        return Response({
            "success": False,
            "message": "Validation Error",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({
            "success": False,
            "message": "Internal Server Error",
            "error": str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def get_product(pk):
    try:
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product)

        return Response({
            "success": True,
            "message": "Data fetched successfully",
            "product": serializer.data
        }, status=status.HTTP_200_OK)

    except Product.DoesNotExist:
        return Response({
            "success": False,
            "message": "Product not found!"
        }, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        return Response({
            "success": False,
            "message": "Internal Server Error",
            "error": str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def update_product(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({
                "success": True,
                "message": "Product updated successfully",
                "product": serializer.data
            }, status=status.HTTP_200_OK)

        return Response({
            "success": False,
            "message": "Validation Error",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    except Product.DoesNotExist:
        return Response({
            "success": False,
            "message": "Product not found!"
        }, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        return Response({
            "success": False,
            "message": "Internal Server Error",
            "error": str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def partial_update_product(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(
            product,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()

            return Response({
                "success": True,
                "message": "Product updated successfully",
                "product": serializer.data
            }, status=status.HTTP_200_OK)

        return Response({
            "success": False,
            "message": "Validation Error",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    except Product.DoesNotExist:
        return Response({
            "success": False,
            "message": "Product not found!"
        }, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        return Response({
            "success": False,
            "message": "Internal Server Error",
            "error": str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def delete_product(pk):
    try:
        product = Product.objects.get(pk=pk)
        product.delete()

        return Response({
            "success": True,
            "message": "Product deleted successfully"
        }, status=status.HTTP_200_OK)

    except Product.DoesNotExist:
        return Response({
            "success": False,
            "message": "Product not found!"
        }, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        return Response({
            "success": False,
            "message": "Internal Server Error",
            "error": str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
