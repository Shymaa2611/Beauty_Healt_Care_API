from django.db import models
import uuid
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from products.models import Product
class Cart(models.Model):
     user=models.OneToOneField(User,on_delete=models.CASCADE)
     id = models.UUIDField(default=uuid.uuid4, primary_key=True)
     created_at = models.DateTimeField(auto_now_add=True)
     def __str__(self):
        return str(self.id)

class cartitems(models.Model):
     cart=models.ForeignKey(Cart,on_delete=models.CASCADE,blank=True,null=True,related_name='cartitems')
     product=models.ForeignKey(Product,on_delete=models.CASCADE,blank=True,null=True,related_name='cartitems')
     quantity=models.PositiveSmallIntegerField(default=0)
     def __str__(self):
         return self.product.product
def create_cart(sender,**kwargs):
    if kwargs['created']:
        user_cart=Cart.objects.create(user=kwargs['instance'])
post_save.connect(create_cart,sender=User)

