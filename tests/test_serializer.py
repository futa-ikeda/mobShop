from django.test import TestCase

from shopping.api.serializer import OrderSerializer
from shopping.models import OrderStatus

class SerializerTestCase(TestCase):

    def setUp(self):
        super().setUp()

    def test_order_serializer_positive(self):
        valid_statuses = [status.value for status in OrderStatus]
        for status in valid_statuses:
            with self.subTest(f'Testing status: {status}'):
                incoming_data = {
                    'status': status
                }
                assert OrderSerializer(data=incoming_data).is_valid(), f'status {status} is not valid!!!'

    def test_order_serializer_negative(self):
        valid_statuses = ['hdkajs', 1]
        for status in valid_statuses:
            with self.subTest(f'Testing status: {status}'):
                incoming_data = {
                    'status': status
                }
                assert not OrderSerializer(data=incoming_data).is_valid(), f'status {status} is not valid!!!'

