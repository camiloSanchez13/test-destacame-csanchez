

from django.db import models

from apps.buses.models.bus import Bus
from apps.drivers.models.drivers import Driver
from apps.routes.models.routes import Route


class Journey(models.Model):

    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name='journeys')
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, related_name='journeys')
    check_out_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)

    @property
    def dispo_seats(self):
        seats = [1, 2, 3 ,4 ,5 ,6 ,7 ,8 ,9 ,10]
        busy = [b['seat'] for b in self.tickets.values('seat')]
        return (set(seats) - set(busy))
