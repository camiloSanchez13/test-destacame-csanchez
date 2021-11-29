from rest_framework import serializers

from apps.buses.serializer.buses_serializer import BusesSerializer
from apps.drivers.serializer.drivers_serializer import DriversSerializer
from apps.journeys.models.journeys import Journey
from apps.routes.serializer.routers_serializer import RoutesSerializer


class JourneysSerializer(serializers.ModelSerializer):
    dispo_seats = serializers.ReadOnlyField()
    class Meta:
        model = Journey
        fields = '__all__'

    def to_representation(self, instance):
        object_ = super(JourneysSerializer, self).to_representation(instance)
        object_['bus'] = BusesSerializer(instance.bus).data
        object_['route'] = RoutesSerializer(instance.route).data
        object_['check_out_time'] = instance.check_out_time.strftime('%Y-%m-%dT%H:%M') if instance.check_out_time else None

        return object_

class JourneysDetailSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    percentage_passengers = serializers.SerializerMethodField()
    check_out_time = serializers.SerializerMethodField()

    class Meta:
        model = Journey
        fields = '__all__'
        depth = 2

    @staticmethod
    def get_check_out_time(obj):
        return obj.check_out_time.strftime('%Y-%m-%dT%H:%M') if obj.check_out_time else None

    @staticmethod
    def get_percentage_passengers(obj):
        return obj.tickets.count() * 10