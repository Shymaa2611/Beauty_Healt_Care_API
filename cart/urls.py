from django.urls import path, include
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register(r'carts', views.CartViewSet)
cart_router = routers.NestedSimpleRouter(router, r'carts', lookup='cart')
cart_router.register(r'items', views.CartItemViewSet, basename='cart-items')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(cart_router.urls)),
]