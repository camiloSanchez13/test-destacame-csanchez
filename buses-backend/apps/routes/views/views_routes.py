from rest_framework import viewsets

from apps.core.pagination import TenResultsPagination
from apps.routes.models.routes import Route
from apps.routes.serializer.routers_serializer import RoutesSerializer


class RoutesViewSet(viewsets.ModelViewSet):


    serializer_class = RoutesSerializer
    queryset = Route.objects.all()
    pagination_class = TenResultsPagination