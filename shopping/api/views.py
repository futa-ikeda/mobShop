from rest_framework import viewsets

from shopping.api.serializer import CartItemSerializer, ProductSerializer
from shopping.models import Product, CartItem


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

# TODO: add OrderViewset