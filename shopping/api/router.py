from rest_framework.routers import DefaultRouter
from shopping.api.views import ProductViewSet

router = DefaultRouter()
router.register(prefix='products', viewset=ProductViewSet)

