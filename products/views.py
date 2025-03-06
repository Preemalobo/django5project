
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsOwnerOrReadOnly, IsVendor  # Keep permissions in users app
from .models import Product
from .serializers import ProductSerializer
from rest_framework.exceptions import PermissionDenied

from users.models import CustomUser

# from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsOwnerOrReadOnly, IsVendor  # Keep permissions in users app
from .models import Product
from .serializers import ProductSerializer
from rest_framework.exceptions import PermissionDenied

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsVendor]

    def perform_create(self, serializer):
        print(f"Authenticated User: {self.request.user}")
        print(f"User is Vendor: {self.request.user.is_vendor}")  # Now it should work fine
              
        if not self.request.user.is_vendor:  # Direct check instead of calling IsVendor()
            print("User does not have permission")
            raise PermissionDenied("Only vendors can create products.")

        print("User has permission, creating product")
        serializer.save(vendor=self.request.user)

class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

class ProductByNameView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        name = self.kwargs["name"]
        return Product.objects.filter(name__iexact=name)

# Create your views here.
