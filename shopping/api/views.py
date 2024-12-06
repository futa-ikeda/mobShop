from rest_framework import viewsets

from shopping.api.permissions import IsSeller
from shopping.api.serializer import CartItemSerializer, ProductSerializer, OrderSerializer
from shopping.models import Product, CartItem, Order


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsSeller]

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

