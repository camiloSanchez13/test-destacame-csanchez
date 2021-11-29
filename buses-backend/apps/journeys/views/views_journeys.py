from django.db.models.aggregates import Count
from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404

from apps.buses.models.bus import Bus
from apps.core.pagination import TenResultsPagination
from apps.journeys.models.journeys import Journey
from apps.journeys.serializer.journeys_serializer import JourneysSerializer, JourneysDetailSerializer
from rest_framework.response import Response

class JourneyViewSet(viewsets.ModelViewSet):


    serializer_class = JourneysSerializer
    queryset = Journey.objects.all()
    pagination_class = TenResultsPagination


    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        try:
            percentage = request.query_params.get('percentage', 0)
            queryset = queryset.annotate(tickets_por=Count('tickets') * 10).filter(tickets_por__gte=percentage)
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = JourneysDetailSerializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            serializer = JourneysDetailSerializer(queryset, many=True)
            return Response(serializer.data)
        except ValueError:
            return Response({"error": "Compruebe el formato del porcentaje"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
