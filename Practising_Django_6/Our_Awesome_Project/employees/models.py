from django.db import models

# Create your models here.


class StaffInfo(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)

    class Meta:
        app_label = 'employees'


class Role(models.Model):
    role = models.CharField(max_length=30)
    location = models.CharField(max_length=30)

    staff = models.ForeignKey(StaffInfo, on_delete=models.CASCADE)

    class Meta:
        app_label = 'employees'

