from rest_framework import serializers

from apps.buses.models.bus import Bus
from apps.drivers.serializer.drivers_serializer import DriversSerializer


class BusesSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    license_plate = serializers.CharField(max_length=6)

    class Meta:
        model = Bus
        fields = '__all__'

    def to_representation(self, instance):
        object_ = super(BusesSerializer, self).to_representation(instance)
        object_['driver'] = DriversSerializer(instance.driver).data

        return object_
