from rest_framework.routers import DefaultRouter
from .views import ProductViewset

router = DefaultRouter()
router.register(prefix='products', viewset=ProductViewset)

