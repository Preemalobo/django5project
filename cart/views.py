from rest_framework import generics, permissions
from cart.models import CartItem
from cart.serializers import CartSerializer
from users.permissions import IsOwnerOrReadOnly

class CartView(generics.ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]



class CartDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
