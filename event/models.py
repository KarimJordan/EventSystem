from django.db import models
from django.utils import timezone
from core.models import TimeStampedModel


class Event(TimeStampedModel):
    name = models.CharField(max_length=200)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)
    venue = models.CharField(max_length=200)
    no_of_guest = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
