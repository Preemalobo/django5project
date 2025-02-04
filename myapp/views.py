from django.shortcuts import render
from rest_framework import generics,permissions
from myapp.permissions import IsVendor
from rest_framework.permissions import IsAuthenticated
from myapp.models import CustomUser,Product
from myapp.serializers import CustomUserSerializer, ProductSerializer


# Create your views here.
class UserRegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated,IsVendor]

#This block of code displays the seller/vendor details whenever new product is created
    def perform_create(self, serializer):
        serializer.save(vendor=self.request.user)

class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAuthenticated, IsVendor]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

#If you are not providing the query set , use def get_queryset
class ProductByNameView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        name = self.kwargs['name']
        return Product.objects.filter(name=name)

