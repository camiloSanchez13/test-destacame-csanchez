from django.db import models

from apps.core.models.persons import Person


class Passenger(Person):

    def __str__(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.full_name