from django.contrib import admin
from .models import Product,Category,Favourite,Brand,Rating

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Favourite)
admin.site.register(Brand)
admin.site.register(Rating)
