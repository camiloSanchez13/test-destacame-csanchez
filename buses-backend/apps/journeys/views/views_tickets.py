from rest_framework import viewsets
from rest_framework.generics import get_object_or_404

from apps.core.pagination import TenResultsPagination
from apps.journeys.models.journeys import Journey
from apps.journeys.models.ticket import Ticket
from apps.journeys.serializer.tickets_serializer import TicketsSerializer


class TicketsViewSet(viewsets.ModelViewSet):


    serializer_class = TicketsSerializer
    queryset = Ticket.objects.all()
    pagination_class = TenResultsPagination


class JourneyTicketViewSet(TicketsViewSet):
    serializer_class = TicketsSerializer


    @property
    def _journey(self) -> Journey:
        return get_object_or_404(Journey, pk=self.kwargs['journey_pk'])

    def get_queryset(self):
        print(self._journey)
        #journey = get_object_or_404(Journey, pk=self.kwargs['bus_pk'])
        return self._journey.tickets.all()