from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=40)
    
class State(models.Model):
    name = models.CharField(max_length=40)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    
class City(models.Model):
    name = models.CharField(max_length=40)
    country = models.ForeignKey(State, on_delete=models.CASCADE)