from rest_framework import serializers
from rest_framework.fields import CharField, DecimalField, IntegerField

from shopping.models import Product


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    name = CharField(max_length=200, required=True)
    price = DecimalField(max_digits=10, decimal_places=2, required=True)
    stock = IntegerField(min_value=0, max_value=100, required=True)
    class Meta:
        model = Product
        fields = ('name', 'price', 'stock')

