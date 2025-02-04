from rest_framework import serializers
from myapp.models import Product,CustomUser

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['id','name','description','price']

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=['id','username','password','is_vendor','is_buyer']
        extra_kwargs={'password':{'write_only':True}}

def create(self,validated_data):
    user=CustomUser(
        username=validated_data['username'],
        is_vendor=validated_data.get('is_vendor',False),
        is_buyer=validated_data.get('is_buyer',False)
    )
    user.set_password(validated_data['password'])
    user.save()
    return user
