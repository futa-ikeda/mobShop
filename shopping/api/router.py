from rest_framework.routers import DefaultRouter
from shopping.api.views import ProductViewSet, CartItemViewSet, OrderViewSet

router = DefaultRouter()
router.register(prefix='products', viewset=ProductViewSet)
router.register(prefix='cart-items', viewset=CartItemViewSet)
router.register(prefix='orders', viewset=OrderViewSet)