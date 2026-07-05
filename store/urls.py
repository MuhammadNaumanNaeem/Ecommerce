from django.urls import path
from .views import CategoryView, CategoryDetailView, ProductView, ProductDetailView

urlpatterns = [
     # Category URLs
    path("categories/", CategoryView.as_view(), name="categories"),
    path("categories/<int:pk>/", CategoryDetailView.as_view(), name="category-detail"),

    # Product URLs
    path("products/", ProductView.as_view(), name="products"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product-detail"),
]