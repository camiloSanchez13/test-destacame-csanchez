from rest_framework import viewsets

from apps.buses.models.bus import Bus
from apps.buses.serializer.buses_serializer import BusesSerializer
from apps.core.pagination import TenResultsPagination


class BusesViewSet(viewsets.ModelViewSet):


    serializer_class = BusesSerializer
    queryset = Bus.objects.all()
    pagination_class = TenResultsPagination
