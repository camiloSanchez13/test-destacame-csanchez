from django.db.models.aggregates import Count, Avg
from rest_framework import serializers

from apps.routes.models.routes import Route


class RoutesSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    average_passengers = serializers.SerializerMethodField()

    class Meta:
        model = Route
        fields = '__all__'

    @staticmethod
    def get_average_passengers(obj : Route) -> float:
        average = obj.journeys.annotate(tickets_s=Count('tickets')).aggregate(avg=Avg('tickets_s'))
        return round(average['avg'], 1) if average['avg'] else 0
