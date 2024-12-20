
from django.urls import path, include

from shopping.api.router import router
from shopping.views.sign_in import sign_in

urlpatterns = [
    path('api/', include(router.urls) ),
    path('sign-in', sign_in),
]
