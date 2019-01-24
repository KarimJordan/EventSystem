from rest_framework import serializers

from .models import Event

from core.serializers import CoreModelSerializer


class EventSerializer(CoreModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
