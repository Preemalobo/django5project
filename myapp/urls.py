from django.urls import path
from myapp.views import ProductListCreateView,ProductRetrieveUpdateDestroyView,UserRegisterView,ProductByNameView

urlpatterns = [
    path('products/', ProductListCreateView.as_view(),name='product_list_create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(),name='product_detail'),
    path('products/name/<str:name>', ProductByNameView.as_view(),name='product_by_name'),
    path('register/', UserRegisterView.as_view(),name='register'),

]