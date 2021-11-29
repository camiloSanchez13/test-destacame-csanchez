from django.db import models
from django.core.validators import MaxValueValidator


class Person(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    rut = models.PositiveIntegerField(validators=[MaxValueValidator(99999999)])
    dv = models.CharField(max_length=1)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.full_name