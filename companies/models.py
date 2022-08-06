from django.db import models
from commons.models import BaseModel
from geolocations.models import City

class Company(BaseModel):
    name = models.CharField(max_length=40)
    commercial_name = models.CharField(max_length=40)
    address = models.CharField(max_length=120)
    phone_number = models.CharField(max_length=12)
    email = models.EmailField(max_length=254, unique=True)
    website = models.URLField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.PROTECT)
    admin = models.OneToOneField('users.Profile', null=True, on_delete=models.SET_NULL)
    
    
class AccessPoint(BaseModel):
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=120)
    email = models.EmailField(max_length=254, unique=True)
    state = models.BooleanField()
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    
class TimeSlot(BaseModel):
    access_point = models.ManyToManyField(AccessPoint)
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)
    start = models.TimeField()
    end = models.TimeField()
    
    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(start__lte=models.F('end')),
                name='start_before_end'
            )
        ]