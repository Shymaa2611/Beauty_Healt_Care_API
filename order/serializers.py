from django.db import transaction
from rest_framework import serializers
from .models import Order,OrderItem
from cart.models import Cart,cartitems



class OrderItemSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = OrderItem 
        fields = ["id", "product", "quantity"]
        


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    class Meta:
        model = Order 
        fields = ['id', "placed_at", "pending_status", "owner", "items"]
        



class CreateOrderSerializer(serializers.Serializer):
    cart_id = serializers.UUIDField()    
    def validate_cart_id(self, cart_id):
        if not Cart.objects.filter(id=cart_id).exists():
            raise serializers.ValidationError("This cart_id is invalid")
        
        elif not cartitems.objects.filter(id=cart_id).exists():
            raise serializers.ValidationError("Sorry your cart is empty")
        
        return cart_id
    
    def save(self, **kwargs):
        with transaction.atomic():
            cart_id = self.validated_data["id"]
            user_id = self.context["user_id"]
            order = Order.objects.create(owner_id = user_id)
            cartitems = cartitems.objects.filter(id=cart_id)
            orderitems = [
                OrderItem(order=order, 
                    product=item.product, 
                    quantity=item.quantity
                    )
            for item in cartitems
            ]
            OrderItem.objects.bulk_create(orderitems)
            return order


class UpdateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order 
        fields = ["pending_status"]