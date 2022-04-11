#from django.db import models
from django.db import models



# Create your models here.

#The docstring code below is what we initially did before moving things around in sub-topic: 'linking models'
"""
class Offenses(models.Model):
    type = models.CharField(max_length=20)
    description = models.TextField(max_length=1000)
    penalty = models.CharField(max_length=20)



class DriverRecords(models.Model):
    points = models.IntegerField()
    valid_driving_licence = models.BooleanField()
    number_of_accidents = models.IntegerField()



class Owner(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    dob = models.DateField()
    gender = models.CharField(max_length=10)



class Car(models.Model):
    color = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    fuel_type = models.CharField(max_length=20)
    registration = models.CharField(max_length=20)
    power = models.IntegerField()
    transmission = models.CharField(max_length=20)
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    number_of_seats = models.CharField(max_length=20)
    engine_cubic_capacity = models.CharField(max_length=20)
    emission_class = models.CharField(max_length=5)
    fuel_consumption = models.IntegerField()
    production_date = models.DateField()

"""

#Linking Models to make relationships




class Owner(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    dob = models.DateField()
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.first_name + "_" + self.last_name


class DriverRecords(models.Model):
    points = models.IntegerField()
    valid_driving_licence = models.BooleanField()
    number_of_accidents = models.IntegerField()

    owner = models.OneToOneField(Owner, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return "Driver record"


class Offenses(models.Model):
    type = models.CharField(max_length=20)
    description = models.TextField(max_length=1000)
    penalty = models.CharField(max_length=20)
    points = models.IntegerField()

    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    def __str__(self):
        return "Offenses"


class Car(models.Model):
    color = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    fuel_type = models.CharField(max_length=20)
    registration = models.CharField(max_length=20)
    power = models.IntegerField()
    transmission = models.CharField(max_length=20)
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    number_of_seats = models.CharField(max_length=20)
    engine_cubic_capacity = models.CharField(max_length=20)
    emission_class = models.CharField(max_length=5)
    fuel_consumption = models.IntegerField()
    production_date = models.DateField()

    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    def __str__(self):
        return "Car"
