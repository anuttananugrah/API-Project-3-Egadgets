from rest_framework import serializers
from api.models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password"]
    def create(self,validated_data):
        return User.objects.create_user(**validated_data)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields="__all__"
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cart
        fields="__all__"
        read_only_fields=["product","user","created_at"]
class OrderSerializer(serializers.ModelSerializer):
    product=ProductSerializer(read_only=True)
    class Meta:
        model=Order
        fields="__all__"
        read_only_fields=["product","user","create_at","status"]

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields="__all__"
        read_only_fields=["product","user","created_at"]