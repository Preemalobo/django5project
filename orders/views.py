
from rest_framework import generics, permissions
from orders.models import Order
from orders.serializers import OrderSerializer
from users.permissions import IsOwnerOrReadOnly  # Import from users app


class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated,IsOwnerOrReadOnly]

    def get_queryset(self):
        """
        Optionally filter orders to show only the ones belonging to the authenticated user.
        """
        return Order.objects.filter(user=self.request.user)


