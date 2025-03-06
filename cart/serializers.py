from rest_framework import serializers
from cart.models import CartItem

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'
