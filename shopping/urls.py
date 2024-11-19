
from django.urls import path, include

from shopping.api.router import router


urlpatterns = [
    path('api/', include(router.urls) ),
]
