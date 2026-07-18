from django.urls import path
from .views import CategoryView, CategoryDetailView, ProductView, ProductDetailView, ProductStatisticsView, CategoryStatisticsView, MonthlyProductStatisticsView, UserStatisticsView, InventoryStatisticsView

urlpatterns = [
     # Category URLs
    path("categories/", CategoryView.as_view(), name="categories"),
    path("categories/<int:pk>/", CategoryDetailView.as_view(), name="category-detail"),

    # Product URLs
    path("products/", ProductView.as_view(), name="products"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product-detail"),

    # Analytics URLs
    path("analytics/products/", ProductStatisticsView.as_view()),
    path("analytics/categories/", CategoryStatisticsView.as_view()),
    path("analytics/monthly-products/", MonthlyProductStatisticsView.as_view()),
    path("analytics/users/", UserStatisticsView.as_view()),
    path("analytics/inventory/", InventoryStatisticsView.as_view()),
]