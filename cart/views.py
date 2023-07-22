from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AddCartItemSerializer, CartItemSerializer,CartSerializer, UpdateCartItemSerializer
from .models import Cart,cartitems
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser

class CartViewSet(CreateModelMixin,RetrieveModelMixin,DestroyModelMixin,viewsets.GenericViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    authentication_classes=(TokenAuthentication)
    permission_classes=(IsAuthenticated)


class CartItemViewSet(viewsets.ModelViewSet):
    
    http_method_names = ["get", "post", "put", "delete"]
    authentication_classes=(TokenAuthentication)
    permission_classes=(IsAuthenticated)
    def get_queryset(self):
        return cartitems.objects.filter(cart_id=self.kwargs.get("pk"))
    
    
    def get_serializer_class(self):
        if self.request.method == "POST":
            return AddCartItemSerializer
        
        elif self.request.method == 'PUT':
            return UpdateCartItemSerializer
        
        return CartItemSerializer
    
    def get_serializer_context(self):
        return {"cart_id": self.kwargs.get("pk")}

