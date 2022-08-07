from django.contrib import admin
from companies.models import Company, AccessPoint, TimeSlot
from geolocations.models import Country, State, City

admin.site.register(Company)
admin.site.register(AccessPoint)
admin.site.register(TimeSlot)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)