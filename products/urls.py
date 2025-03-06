from django.urls import path
from products.views import ProductListCreateView, ProductRetrieveUpdateDestroyView, ProductByNameView

urlpatterns = [
    path('', ProductListCreateView.as_view(), name='product-list-create'),
    path('<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-detail'),
    path('name/<str:name>/', ProductByNameView.as_view(), name='product-by-name'),
]
