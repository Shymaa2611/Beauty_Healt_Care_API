from rest_framework import serializers
from products.models import Product
from products.serializers import productSerializer
from .models import Cart,cartitems

class CartItemSerializer(serializers.ModelSerializer):
    product =productSerializer(many=False)
    sub_total = serializers.SerializerMethodField( method_name="total")
    class Meta:
        model= cartitems
        fields = ["id", "cart", "product", "quantity", "sub_total"]
        
    
    def total(self, cartitem:cartitems):
        return cartitem.quantity * cartitem.product.product_price
    

class AddCartItemSerializer(serializers.ModelSerializer):
    def save(self, **kwargs):
        cart_id = self.context.get("id")
        id= self.validated_data.get("id")
        quantity = self.validated_data["quantity"] 
        
        try:
            cartitem = cartitems.objects.get(Product.objects.get(id=id),id=cart_id)
            cartitem.quantity += quantity
            cartitem.save()
            
            self.instance = cartitem
        except:
            
            self.instance = cartitems.objects.create(id=cart_id, **self.validated_data)
            
        return self.instance
         

    class Meta:
        model = cartitems
        fields = ["id", "product", "quantity"]

class UpdateCartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = cartitems
        fields = ["quantity"]


class CartSerializer(serializers.ModelSerializer):
    #id = serializers.UUIDField(read_only=True,ValueError=)
    items = CartItemSerializer(many=True, read_only=True)
    grand_total = serializers.SerializerMethodField(method_name='main_total')
    
    class Meta:
        model = Cart
        fields = ["id", "items", "grand_total"] 
    
    def main_total(self, cart: Cart):
        items = cart.items.all()
        total = sum([item.quantity * item.product.price for item in items])
        return total
            
        
