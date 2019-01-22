from django.db import models
from django.contrib.auth.models import User


# timestamped abstract model class
class TimeStampedModel(models.Model):
    created = models.DateField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name="%(app_label)s_%(class)s_created_by")
    modified = models.DateField(auto_now_add=True)
    modified_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name="%(app_label)s_%(class)s_modified_by")

    class Meta:
        abstract = True
