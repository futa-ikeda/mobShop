from rest_framework import viewsets

from shopping.api.serializer import ProductSerializer
from shopping.models import Product


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer