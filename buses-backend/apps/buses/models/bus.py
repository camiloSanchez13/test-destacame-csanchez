
from django.db import models

from apps.drivers.models.drivers import Driver


class Bus(models.Model):

    admission_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    license_plate = models.CharField(max_length=6, unique=True)
    driver = models.OneToOneField(Driver, on_delete=models.CASCADE, related_name='bus')
    def __str__(self):
        return self.license_plate

    def save(self, *args, **kwargs):
        self.license_plate = str(self.license_plate).upper()
        super().save(*args, **kwargs)