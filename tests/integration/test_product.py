
from django.contrib.auth.models import User, Group
from django.urls import reverse
from rest_framework.test import APITestCase


class ProductTestCase(APITestCase):

    def setUp(self): # since Djago uses its own test db for tests, create user and credentials and use that
        self.user = User.objects.create_user('testSellerUser_product', email=None, password='mobshop1')
        buyer_group = Group.objects.create(name='seller')
        self.user.groups.add(buyer_group)
        self.user.save()
        self.client.login(username='testSellerUser_product', password='mobshop1')

    def testGetProduct(self):
        response = self.client.get(reverse('product-list'))  #<-- using 'reverse' so we are not dependent on the hard corded path .. as we may change in development and ont have to keep u with it..
                                                             #<-- remember that Django does this model-details but because we are pulling all of it (and os the list)
        self.assertEqual(response.status_code, 200)

# next level of testing: create product and assert







