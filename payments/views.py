from rest_framework import generics, permissions
from payments.models import Payment
from payments.serializers import PaymentSerializer
from users.permissions import IsOwnerOrReadOnly

class PaymentView(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]



class PaymentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
