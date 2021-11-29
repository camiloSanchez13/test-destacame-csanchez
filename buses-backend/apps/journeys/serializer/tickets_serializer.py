from rest_framework import serializers

from apps.journeys.models.ticket import Ticket
from apps.passengers.serializer.passengers_serializer import PassengersSerializer


class TicketsSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Ticket
        fields = '__all__'



    def to_representation(self, instance):
        object_ = super(TicketsSerializer, self).to_representation(instance)
        object_['passenger'] = PassengersSerializer(instance.passenger).data

        return object_

    def validate(self, attrs):
        journey = attrs['journey']
        ticket_pk = self.instance.id if self.instance else None
        passenger = attrs['passenger']

        if journey.tickets.all().exclude(pk=ticket_pk).count() >= 10:
            raise serializers.ValidationError({'ticket': ["No hay tickets disponible"]})
        elif journey.tickets.filter(seat=attrs['seat']).exclude(pk=ticket_pk).first():
            raise serializers.ValidationError({'seat': ["Error asiendo ocupado"]})
        elif journey.tickets.filter(passenger=passenger).exists() and not ticket_pk:
            raise serializers.ValidationError({'passenger': ["El pasajero ya contiene un asiento"]})

        return attrs
