from rest_framework import serializers

from .models import Event

from core.serializers import CoreModelSerializer


class EventSerializer(CoreModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'name', 'venue', 'no_of_guest', 'start_date', 'end_date')
