from rest_framework import serializers

from apps.buses import models
from apps.drivers.models.drivers import Driver


class DriversSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Driver
        fields = '__all__'