from decimal import Decimal

from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.name}'

class CartItem(models.Model):
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    @property
    def total (self):
        return self.item.price *  self.quantity

    def save(self, **kwargs):
        product = self.item
        product.stock = product.stock - self.quantity
        product.save()
        super().save(**kwargs)


class OrderStatus(models.enums.Choices):
    PENDING = 'pending'
    COMPLETED = 'completed'

class Order(models.Model):
    items = models.ForeignKey(CartItem, on_delete=models.DO_NOTHING)
    status = models.CharField(OrderStatus, max_length=20)

