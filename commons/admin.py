from django.contrib import admin
from companies.models import Company, AccessPoint, TimeSlot
from users.models import Profile

admin.site.register(Company)
admin.site.register(AccessPoint)
admin.site.register(TimeSlot)