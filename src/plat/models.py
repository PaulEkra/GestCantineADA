from django.db import models

from base.models.helpers.named_date_time_model import NamedDateTimeModel


# Create your models here.
class PlatModel(NamedDateTimeModel):
    summary = models.CharField(max_length=255)

    def __str__(self):
        return self.name
