from django.db import models

from base.models.helpers.date_time_model import DateTimeModel


# Create your models here.
class MenuModel(DateTimeModel):
    plat = models.OneToOneField('plat.PlatModel', on_delete=models.CASCADE)

