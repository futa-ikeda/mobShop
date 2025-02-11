from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField, DecimalField, IntegerField

from shopping.models import Product, CartItem, Order, OrderStatus


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
        buyer = self.context['request'].user
        if not buyer:
            raise ValidationError('not authorised')
        validated_data['buyer'] = buyer
        return super().create(validated_data)


    class Meta:
        model = CartItem
        fields = ('item', 'quantity', 'url', 'total', 'order')



def validate_status(value):
    if value not in OrderStatus:
        raise ValidationError('This is not valid status')

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    status = CharField(max_length=20, default=OrderStatus.PENDING, validators=[validate_status],)

    def create(self, validated_data):
        buyer = self.context['request'].user
        cartitems = buyer.cartitem_set.filter(order=None)
        if not cartitems:
            raise ValidationError('cart is empty')
        order = super().create(validated_data)
        for item in cartitems:
            item.order = order
            item.save()
        return order

    class Meta:
        model = Order
        fields = ('id', 'status', 'url')



