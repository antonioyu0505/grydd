from django.db import models
from django.contrib.auth.models import AbstractUser
from commons.models import BaseModel
from geolocations.models import City

class Profile(AbstractUser, BaseModel):
    phone_number = models.CharField(max_length=12)
    address = models.CharField(max_length=120)
    city = models.ForeignKey(City, null=True, on_delete=models.PROTECT)
    company_id = models.ForeignKey('companies.Company', null=True, on_delete=models.SET_NULL)