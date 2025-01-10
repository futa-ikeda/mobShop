
from django.contrib.auth.models import User, Group
from django.urls import reverse
from rest_framework.test import APITestCase

from shopping.models import Product


class ProductTestCase(APITestCase):

    def setUp(self): # since Djago uses its own test db for tests, create user and credentials and use that
        self.user = User.objects.create_user('testSellerUser_product', email=None, password='mobshop1')
        self.seller_group = Group.objects.create(name='seller')
        self.user.groups.add(self.seller_group)
        self.user.save()
        self.client.login(username='testSellerUser_product', password='mobshop1')

    def testGetProduct(self):
        response = self.client.get(reverse('product-list'))  #<-- using 'reverse' so we are not dependent on the hard corded path .. as we may change in development and ont have to keep u with it..
                                                             #<-- remember that Django does this model-details but because we are pulling all of it (and os the list)
        self.assertEqual(response.status_code, 200)

# next level of testing: create product and assert
    def testProductDetail(self):
        first_product = Product.objects.create(name='pencils', price=0.10, stock=100)
        test_product = Product.objects.create(name='pens',price=0.25,stock=100)
        response = self.client.get(reverse('product-detail', args = [test_product.id]))
        self.assertEqual(response.status_code, 200, 'Incorrect status code')
        self.assertEqual(response.data['id'], test_product.id, 'Incorrect id')
        self.assertEqual(response.data['name'], 'pens', 'Incorrect name')
        self.assertEqual(response.data['price'], '0.25', 'Incorrect price')
        self.assertEqual(response.data['stock'], 100, 'Incorrect stock')

    def testBuyerPermission(self):
        self.user.groups.remove(self.seller_group)
        buyer_group = Group.objects.create(name='buyer')
        self.user.groups.add(buyer_group)
        self.user.save()
        response = self.client.get(reverse('product-list'))
        self.assertEqual(response.status_code, 403, 'Buyers are not allowed')

