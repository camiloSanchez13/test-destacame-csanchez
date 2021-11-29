from django.db import models



class Route(models.Model):

    origin = models.CharField(max_length=100)
    destiny = models.CharField(max_length=100)