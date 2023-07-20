from django.db import models
from django.contrib.auth.models import  User
from django.db.models.signals import post_save
from django.utils.text import slugify

gender_info=[
    ("male","male"),
    ("female","female")
]

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    user_image=models.ImageField(upload_to='user/avater/',blank=True,null=True)
    first_name=models.CharField(max_length=30,verbose_name='First Name')
    last_name=models.CharField(max_length=30,verbose_name='Last Name')
    email=models.CharField(max_length=100,verbose_name='Email',blank=True,null=True)
    gender=models.CharField(max_length=10,choices=gender_info,verbose_name='Gender',blank=True,null=True)
    phone=models.CharField(max_length=15,verbose_name='Phone Number',blank=True,null=True)
    skin_type=models.CharField(max_length=50,verbose_name='Skin Type',blank=True,null=True)
    skin_ton=models.CharField(max_length=50,verbose_name='Skin Ton',blank=True,null=True)
    skin_concern=models.CharField(max_length=50,verbose_name='Skin Concern',blank=True,null=True)
    hair_type=models.CharField(max_length=50,verbose_name='hair type',blank=True,null=True)
    address=models.CharField(max_length=50,verbose_name='Address',blank=True,null=True)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now_add=True)
    slug=models.SlugField(blank=True,null=True)
    def __str__(self):
        return self.slug
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.user.username)
        super(Profile,self).save(*args,**kwargs)
    

def create_profile(sender,**kwargs):
    if kwargs['created']:
        user_profile=Profile.objects.create(user=kwargs['instance'])
post_save.connect(create_profile,sender=User)


