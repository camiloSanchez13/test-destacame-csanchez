from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from apps.journeys.models.journeys import Journey
from apps.passengers.models.passengers import Passenger


class Ticket(models.Model):

    journey = models.ForeignKey(Journey, on_delete=models.CASCADE, related_name='tickets')
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE, related_name='tickets')
    seat = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    sale_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
