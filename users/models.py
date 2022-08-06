from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from commons.models import BaseModel
from geolocations.models import City

class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=12)
    address = models.CharField(max_length=120)
    city = models.ForeignKey(City, on_delete=models.PROTECT)
    company_worked = models.ForeignKey('companies.Company', null=True, on_delete=models.SET_NULL)

@receiver
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
