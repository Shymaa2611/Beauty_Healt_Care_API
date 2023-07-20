from rest_framework import serializers
from .models import Product,Category,Brand,Favourite,Rating
class productSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['product','product_desc','product_type','product_image','product_price','product_size','create_at','update_at','category','Brand','no_of_rating','avg_rating']

class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'
class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model=Brand
        fields='__all__'
class ratingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Rating
        fields='__all__'

class favouriteSerializer(serializers.ModelSerializer):
    product=productSerializer()
    class Meta:
        model=Favourite
        fields='__all__'


