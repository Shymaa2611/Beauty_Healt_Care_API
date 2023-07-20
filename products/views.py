from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import  rest_framework.status  as status
from .models import Rating,Category,Favourite,Product,Brand
from .serializers import productSerializer,ratingSerializer,favouriteSerializer
from django.contrib.auth.models import User

@api_view(['GET','POST'])
def get_add_product_data(request):
    if request.method=='GET':
        product=Product.objects.all()
        serializer =productSerializer(product, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer =productSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def update_product_data(request,slug):
    try:
        product =Product.objects.get(slug=slug)
    except Product.DoesNotExists:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = productSerializer(product,many=False)
        return Response(serializer.data)
        
    elif request.method == 'PUT':
        serializer = productSerializer(product, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        product.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
    
@api_view(['GET'])
def seach_about_product(request):
     data = Product.objects.filter(
       product=request.data['product']
    )
     serializer=productSerializer(data,many=True)
     return Response(serializer.data)
@api_view(['GET','POST'])
def product_rate(request, slug):

    if 'stars' in request.data:
            product = Product.objects.get(slug=slug)
            stars = request.data['stars']
            username = request.data['username']
            user = User.objects.get(username=username)
            try:
                rating = Rating.objects.get(user=user, product=product.slug) 
                rating.stars = stars
                rating.save()
                serializer =ratingSerializer(rating, many=False)
                json = {
                    'message': 'product Rate is Updated',
                    'result': serializer.data
                }
                return Response(json , status=status.HTTP_201_CREATED)

            except:
                rating = Rating.objects.create(stars=stars, product=product, user=user)
                serializer=ratingSerializer(rating, many=False)
                json = {
                    'message': 'product Rate is Created',
                    'result': serializer.data
                }
                return Response(json , status=status.HTTP_200_OK)

    else:
            json = {
                'message': 'is not valid'
            }
            return Response(json , status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def product_favorite(request, slug):

    if 'love' in request.data :
            product = Product.objects.get(slug=slug)
            love = request.data['love']
            username = request.data['username']
            user = User.objects.get(username=username)
            try:
                favoutite = Favourite.objects.get(user=user, product=product.slug) 
                favoutite.love = love
                favoutite.save()
                serializer =favouriteSerializer(favoutite , many=False)
                json = {
                    'message': 'product favourite is Updated',
                    'result': serializer.data
                }
                return Response(json , status=status.HTTP_201_CREATED)

            except:
                favoutite = Favourite.objects.create(love=love, product=product, user=user)
                serializer=favouriteSerializer(favoutite, many=False)
                json = {
                    'message': 'product favoutite is Created',
                    'result': serializer.data
                }
                return Response(json , status=status.HTTP_200_OK)

    else:
            json = {
                'message': 'is not valid'
            }
            return Response(json , status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_favourite_products(request):
     data=Favourite.objects.filter(
         love=1
     )
     serializer=favouriteSerializer(data,many=True)
     return Response(serializer.data)

@api_view(['GET'])
def get_recommended_products(request,slug):
     try:
          product = Product.objects.get(slug=slug)
          related_products = Product.objects.filter(category__exact=product.category).exclude(slug=slug)[:4]
          serializer = productSerializer(related_products, many=True)
          return Response(serializer.data)
     except Product.DoesNotExist:
          return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_new_products(request):
    product=Product.objects.all()
    product=product.order_by('-create_at')[:10]
    serializer =productSerializer(product, many=True)
    return Response(serializer.data)
     
