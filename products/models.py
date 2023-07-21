from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator
from django.utils.text import slugify

class Product(models.Model):
    product=models.CharField(max_length=30)
    product_desc=models.TextField(verbose_name='Description',blank=True,null=True)
    product_type=models.CharField(max_length=30,verbose_name='Type')
    product_image=models.ImageField(upload_to='products/',verbose_name='Image',blank=True,null=True)
    product_price=models.DecimalField(max_digits=10,decimal_places=2,verbose_name='Price')
    product_discont=models.DecimalField(max_digits=10,decimal_places=2,verbose_name='Discont',blank=True,null=True)
    product_size=models.CharField(max_length=30,verbose_name='Size')
    quantity=models.IntegerField(default=0)
    create_at=models.DateField(auto_now_add=True,verbose_name='Created_At')
    update_at=models.DateField(auto_now_add=True,verbose_name='Update_At')
    category=models.ForeignKey('Category',on_delete=models.CASCADE,related_name='Product')
    Brand=models.ForeignKey('Brand',on_delete=models.CASCADE,related_name='Product')
    slug=models.SlugField(blank=True,null=True)
    def no_of_rating(self):
        no_ratings=Rating.objects.filter(product=self).count()
        return no_ratings
    def avg_rating(self):
        sum_ratings=0
        ratings=Rating.objects.filter(product=self)
        for rate in ratings:
            sum_ratings+=rate.stars
        count_value=Rating.objects.filter(product=self).count()
        if count_value==0:
               count_value=1  
        return sum_ratings/count_value
    def __str__(self):
        return self.slug
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.product)
        super(Product,self).save(*args,**kwargs)
    
class Category(models.Model):
    category_name=models.CharField(max_length=30,verbose_name='Category')
    category_icon=models.ImageField(upload_to='category',blank=True,null=True)
    create_at=models.DateField(auto_now_add=True,verbose_name='Created_At')
    update_at=models.DateField(auto_now_add=True,verbose_name='Update_At')
    def __str__(self):
        return self.category_name

class Brand(models.Model):
    Brand_name=models.CharField(max_length=30,verbose_name='Brand')
    Brand_icon=models.ImageField(upload_to='brand',blank=True,null=True)
    def __str__(self):
        return self.Brand_name

class Rating(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    stars=models.IntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(5)])
    class Meta:
        unique_together=(('user','product'))
        index_together=(('user','product'))
    def __str__(self):
        return str(self.stars)

class Favourite(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    love=models.IntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    def __str__(self):
        return str(self.love)
