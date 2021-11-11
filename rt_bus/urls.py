from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from rt_bus import api

router = routers.SimpleRouter()
router.register('bus', api.BusViewSet)
router.register('route', api.RouteViewSet)

urlpatterns = [
    path('api/', include(router.urls))
]