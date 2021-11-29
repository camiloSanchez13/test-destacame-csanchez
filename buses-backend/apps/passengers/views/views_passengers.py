from rest_framework import viewsets

from apps.core.pagination import TenResultsPagination
from apps.passengers.models.passengers import Passenger
from apps.passengers.serializer.passengers_serializer import PassengersSerializer


class PassengersViewSet(viewsets.ModelViewSet):


    serializer_class = PassengersSerializer
    queryset = Passenger.objects.all()
    pagination_class = TenResultsPagination