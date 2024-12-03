from django.db.models import ForeignKey
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField, DecimalField, IntegerField
from rest_framework.relations import RelatedField

from shopping.models import Product, CartItem, Order


class ProductSerializer(serializers.HyperlinkedModelSerializer):

    name = CharField(max_length=200, required=True)
    price = DecimalField(max_digits=10, decimal_places=2, required=True)
    stock = IntegerField(min_value=0, max_value=100, required=True)

    class Meta:
        model = Product
        fields = ('id','name', 'price', 'stock', 'url')

class CartItemSerializer(serializers.HyperlinkedModelSerializer):
    quantity = IntegerField(min_value=1, required=True)
    total = DecimalField(decimal_places=2, max_digits=10, read_only=True)


    def create(self, validated_data):
        product = validated_data['item']
        if validated_data['quantity'] > product.stock:
            raise ValidationError('Too many')
        return super().create(validated_data)

    class Meta:
        model = CartItem
        fields = ('item', 'quantity', 'url', 'total', 'order')

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    status = CharField(max_length=20, read_only=True)
    class Meta:
        model = Order
        fields = ('id', 'status', 'url')
