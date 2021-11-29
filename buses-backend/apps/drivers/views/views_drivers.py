from rest_framework import viewsets

from apps.core.pagination import TenResultsPagination
from apps.drivers.models.drivers import Driver
from apps.drivers.serializer.drivers_serializer import DriversSerializer


class DriversViewSet(viewsets.ModelViewSet):


    serializer_class = DriversSerializer
    queryset = Driver.objects.all()
    pagination_class = TenResultsPagination