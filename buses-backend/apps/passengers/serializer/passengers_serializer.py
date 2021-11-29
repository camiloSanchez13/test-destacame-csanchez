from rest_framework import serializers

from apps.passengers.models.passengers import Passenger


class PassengersSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Passenger
        fields = '__all__'