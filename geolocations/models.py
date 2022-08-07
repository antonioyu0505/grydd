from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=40)
    
    def __str__(self) -> str:
        return self.name
    
class State(models.Model):
    name = models.CharField(max_length=40)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name
    
class City(models.Model):
    name = models.CharField(max_length=40)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name