from django.db.models import Count, Avg, Sum, F
from django.db.models.functions import TruncMonth
from rest_framework.response import Response
from rest_framework import status

from .models import Product, Category
from accounts.models import User


def product_statistics():
    try:
        stats = Product.objects.aggregate(
            total_products=Count("id"),
            average_price=Avg("price"),
            total_stock=Sum("stock"),
        )

        return Response(
            {
                "success": True,
                "message": "Product statistics fetched successfully.",
                "data": stats,
            },
            status=status.HTTP_200_OK,
        )

    except Exception as e:
        return Response(
            {
                "success": False,
                "message": "Failed to fetch product statistics.",
                "error": str(e),
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


def category_statistics():
    try:
        categories = (
            Category.objects.annotate(
                total_products=Count("products")
            )
            .values("name", "total_products")
            .order_by("name")
        )

        return Response(
            {
                "success": True,
                "message": "Category statistics fetched successfully.",
                "data": list(categories),
            },
            status=status.HTTP_200_OK,
        )

    except Exception as e:
        return Response(
            {
                "success": False,
                "message": "Failed to fetch category statistics.",
                "error": str(e),
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


def monthly_product_statistics():
    try:
        monthly = (
            Product.objects
            .annotate(month=TruncMonth("created_at"))
            .values("month")
            .annotate(total_products=Count("id"))
            .order_by("month")
        )

        labels = []
        totals = []

        for item in monthly:
            labels.append(item["month"].strftime("%B %Y"))
            totals.append(item["total_products"])

        return Response(
            {
                "success": True,
                "message": "Monthly statistics fetched successfully.",
                "data": {
                    "labels": labels,
                    "totals": totals,
                },
            },
            status=status.HTTP_200_OK,
        )

    except Exception as e:
        return Response(
            {
                "success": False,
                "message": "Failed to fetch monthly statistics.",
                "error": str(e),
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


def user_statistics():
    try:
        data = {
            "total_users": User.objects.count(),
            "active_users": User.objects.filter(is_active=True).count(),
            "inactive_users": User.objects.filter(is_active=False).count(),
            "admins": User.objects.filter(role="admin").count(),
            "users": User.objects.filter(role="user").count(),
        }

        return Response(
            {
                "success": True,
                "message": "User statistics fetched successfully.",
                "data": data,
            },
            status=status.HTTP_200_OK,
        )

    except Exception as e:
        return Response(
            {
                "success": False,
                "message": "Failed to fetch user statistics.",
                "error": str(e),
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


def inventory_statistics():
    try:
        products = Product.objects.aggregate(
            inventory_value=Sum(F("price") * F("stock")),
            average_price=Avg("price"),
        )

        return Response(
            {
                "success": True,
                "message": "Inventory statistics fetched successfully.",
                "data": products,
            },
            status=status.HTTP_200_OK,
        )

    except Exception as e:
        return Response(
            {
                "success": False,
                "message": "Failed to fetch inventory statistics.",
                "error": str(e),
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )