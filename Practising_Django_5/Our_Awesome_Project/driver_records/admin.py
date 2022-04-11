
from django.contrib import admin
from .models import Offenses, DriverRecords, Owner, Car

# Register your models here.

admin.site.register(Offenses)
admin.site.register(Car)
admin.site.register(Owner)
admin.site.register(DriverRecords)

