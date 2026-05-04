from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet,ViewSet
from rest_framework import status
from api.models import *
from api.serializers import *
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.authentication import BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import obtain_auth_token

# Create your views here.

class UserViewSet(ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer

    def list(self,request):
        return Response(data={"msg":"Not Allowd"},status=status.HTTP_406_NOT_ACCEPTABLE)
    def retrieve(self,request):
        return Response(data={"msg":"Not Allowd"},status=status.HTTP_406_NOT_ACCEPTABLE)
    def destroy(self,request):
        return Response(data={"msg":"Not Allowd"},status=status.HTTP_406_NOT_ACCEPTABLE)
    
    
# all products localhost:8000/products/
    
class ProductViewSet(ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get_queryset(self):
        # queryset = Product.objects.all()
        # category = self.request.query_params.get('category')
        # print(category)  
        # if category:
        #     queryset = queryset.filter(category__iexact=category)
        # return queryset
        qs=self.queryset
        if self.request.query_params:
          qs=qs.filter(category=self.request.query_params.get('category'))
        return qs 
    
    def create(self,request):
        return Response(data={"msg":"Not Allowd"},status=status.HTTP_406_NOT_ACCEPTABLE)
    def update(self,request,pk=0):
        return Response(data={"msg":"Not Allowd"},status=status.HTTP_406_NOT_ACCEPTABLE)
    def partial_update(self,request,pk=0):
        return Response(data={"msg":"Not Allowd"},status=status.HTTP_406_NOT_ACCEPTABLE)
    def destroy(self,request,pk=0):
        return Response(data={"msg":"Not Allowd"},status=status.HTTP_406_NOT_ACCEPTABLE)

    @action(methods=["POST"],detail=True)
    def addtocart(self,request,pk=0):
        user=request.user
        product=self.get_object()
        dser=CartSerializer(data=request.data)
        if dser.is_valid():
            dser.save(user=user,product=product)
            return Response(data=dser.data,status=status.HTTP_200_OK)
        return Response(data=dser.errors,status=status.HTTP_400_BAD_REQUEST)
    @action(methods=["POST"],detail=True)
    def addreview(self,request):
        user=request.user
        product=self.get_object()
        dser=ReviewSerializer(data=request.data)
        if dser.is_valid():
            dser.save(user=user,product=product)
            return Response(data=dser.data,status=status.HTTP_200_OK)
        return Response(data=dser.errors,status=status.HTTP_400_BAD_REQUEST)
# modelview

# http://localhost:8000/cartlist

class CartViewSet(ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    serializer_class=CartSerializer
    queryset=Cart.objects.all()
    
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    
    def create(self,request):
        return Response(data={"msg":"Not Allowd"},status=status.HTTP_406_NOT_ACCEPTABLE)
    def update(self,request,pk=0):
        return Response(data={"msg":"Not Allowd"},status=status.HTTP_406_NOT_ACCEPTABLE)
    def partial_update(self,request,pk=0):
        return Response(data={"msg":"Not Allowd"},status=status.HTTP_406_NOT_ACCEPTABLE)
    
    def placeorder(self,request,pk=0):
        user=request.user
        product=self.get_object().product
        dser=OrderSerializer(data=request.data)
        if dser.is_valid():
            dser.save(user=user,product=product)
            Cart.objects.get(id=self.get_object().id).delete()
            return Response(data=dser.data,status=status.HTTP_200_OK)
        return Response(data=dser.errors,status=status.HTTP_400_BAD_REQUEST)
    
# localhost:8000/orders

class OrderViewSet(ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    serializer_class=OrderSerializer
    queryset=Order.objects.all()

    def get_queryset(self):
        qs=self.queryset.filter(user=self.request.user)
        return qs
    def create(self,request):
        return Response(data={"msg":"Not Allowd"},status=status.HTTP_406_NOT_ACCEPTABLE)
    def update(self,request,pk=0):
        return Response(data={"msg":"Not Allowd"},status=status.HTTP_406_NOT_ACCEPTABLE)
    def partial_update(self,request,pk=0):
        return Response(data={"msg":"Not Allowd"},status=status.HTTP_406_NOT_ACCEPTABLE)
    def destroy(self,request,pk=0):
        return Response(data={"msg":"Not Allowd"},status=status.HTTP_406_NOT_ACCEPTABLE)
    
class ReviewViewSet(ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    serializer_class=ReviewSerializer
    queryset=Review.objects.all()

    def get_queryset(self):
        qs=self.queryset.filter(user=self.request.user)
        return qs
    def create(self,request):
        return Response(data={"msg":"Not Allowd"},status=status.HTTP_406_NOT_ACCEPTABLE)
    def update(self,request,pk=0):
        return Response(data={"msg":"Not Allowd"},status=status.HTTP_406_NOT_ACCEPTABLE)
    def partial_update(self,request,pk=0):
        return Response(data={"msg":"Not Allowd"},status=status.HTTP_406_NOT_ACCEPTABLE)
    def destroy(self,request,pk=0):
        return Response(data={"msg":"Not Allowd"},status=status.HTTP_406_NOT_ACCEPTABLE)
    
    @action(methods=["PATCH"],detail=True)
    def cancellorder(self,request,pk=0):
        order=self.get_object()
        order.status="Cancelled"
        order.save()
        return Response(data={"msg":"Order Cancelled"},status=status.HTTP_200_OK)