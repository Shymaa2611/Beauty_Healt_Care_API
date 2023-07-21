from django.urls import path
from . import views
urlpatterns=[
   path('api/get_data/',views.get_add_product_data,name='product_data'),
   path('api/get_data/<slug:slug>/',views.update_product_data,name='product_data'),
   path('api/search/',views.seach_about_product,name='search'),
   path('api/get_favourite/',views.get_favourite_products,name='get_favourite'),
   path('api/rate/<slug:slug>/',views.product_rate,name='rating'),
   path('api/favourite/<slug:slug>/',views.product_favorite,name='favourite'),
   path('api/recommanded/<slug:slug>/',views.get_recommended_products,name='recommended'),
   path('api/get_new_product/',views.get_new_products,name='get_new_product'),
   path('api/get_product_category/',views.get_product_category,name='get_product_category')

]
