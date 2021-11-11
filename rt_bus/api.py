from azure.messaging.webpubsubservice import WebPubSubServiceClient
from azure.messaging.webpubsubservice.rest import *
from rt_bus_server import settings
from rest_framework import viewsets, permissions
from rt_bus.models import Bus, Route
from rt_bus.serializers import BusSerializer, RouteSerializer

class BusViewSet(viewsets.ModelViewSet):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer
    permissions = [permissions.AllowAny]

    def partial_update(self, request, pk=None):
        if 'lat' in request.data and 'lng' in request.data:
            connection_string = settings.WEB_PUBSUB_CONNECTION_STRING
            hub_name = settings.WEB_PUBSUB_HUB_NAME
            service_client = WebPubSubServiceClient.from_connection_string(connection_string)
            res = service_client.send_request(build_send_to_all_request(
                hub_name,
                content=f'Lat: {request.data["lat"]} Lng: {request.data["lng"]}',
                content_type='text/plain'
            ))
            # res should be <HttpResponse: 202 Accepted>
            print(res)
        return super().partial_update(request, pk)
        

class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    permissions = [permissions.AllowAny]