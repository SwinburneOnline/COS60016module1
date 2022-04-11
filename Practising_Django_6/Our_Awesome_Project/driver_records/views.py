from django.shortcuts import render
#from django.http import HttpResponse

from django.http import HttpResponse
#from django.views.decorators.http import require_http_methods


from django.views.decorators.http import require_http_methods
from .models import Offenses, DriverRecords, Owner, Car



# Create your views here.


def test_view(request):
    html = "<html><body>IT WORKS!!!</body></html>"
    return HttpResponse(html)
@require_http_methods(["GET"])
def records(request):
    pass


@require_http_methods(["GET"])
def records(request):
    offenses = Offenses.objects.all()
    driver_records = DriverRecords.objects.all()
    owners = Owner.objects.all()
    car = Car.objects.all()

    name = []
    for owner in owners:
        print(owner.first_name)
        name.append(owner.first_name)

    context = {
        "offenses": offenses,
        "driver_records": driver_records,
        "owner": owners,
        "car": car,
        "name": name,
    }

    return render(request, "records.html", context)



#New views below since refactoring the app name to driver_records

@require_http_methods(["GET"])
def populate_with_sample_data(request):
    owner_1 = Owner(first_name="Bruce",
                    last_name="Tail",
                    dob=datetime.date(1997, 10, 19),
                    gender="Male")
    owner_1.save()

    dr_1 = DrivingRecords(points=2,
                          valid_driving_licence=True,
                          number_of_accidents=0,
                          owner=owner_1)
    dr_1.save()

    offense_1 = Offenses(type="speeding",
                         description=("Drove 5 miles an hour over the speed limit"),
                         penalty="One point on the license and a 50$ fine",
                         points=1, owner=owner_1)
    offense_1.save()

    car_1 = Car(color='Black',
                type='Sedan',
                fuel_type='Petrol',
                registration='234-0-33233',
                power=300,
                transmission='automatic',
                make='BMW',
                model='m3',
                number_of_seats='5',
                engine_cubic_capacity='3000cc',
                emission_class='EUR 6',
                fuel_consumption=9,
                production_date=datetime.date(2020, 1, 1),
                owner=owner_1
                )
    car_1.save()

    ######################################################################

    owner_2 = Owner(first_name="John",
                    last_name="Doe",
                    dob=datetime.date(1987, 11, 19),
                    gender="Male")
    owner_2.save()

    dr_2 = DrivingRecords(points=0,
                          valid_driving_licence=True,
                          number_of_accidents=0,
                          owner=owner_2)
    dr_2.save()

    offense_2 = Offenses(type="speeding",
                         description=("Drove 1 mile an hour over the speed limit"),
                         penalty="Warning",
                         points=0, owner=owner_2)
    offense_2.save()

    car_2 = Car(color='White',
                type='Sedan',
                fuel_type='Petrol',
                registration='2ww34-0-333',
                power=200,
                transmission='automatic',
                make='Audi',
                model='a4',
                number_of_seats='5',
                engine_cubic_capacity='2000cc',
                emission_class='EUR 6',
                fuel_consumption=6,
                production_date=datetime.date(2019, 1, 1),
                owner=owner_2
                )
    car_2.save()

    ######################################################################

    owner_3 = Owner(first_name="Jane",
                    last_name="Doe",
                    dob=datetime.date(1986, 1, 19),
                    gender="Female")
    owner_3.save()

    dr_3 = DrivingRecords(points=10,
                          valid_driving_licence=False,
                          number_of_accidents=1,
                          owner=owner_3)
    dr_3.save()

    offense_3 = Offenses(type="speeding",
                         description=("Drove 15 miles an hour over the speed limit"),
                         penalty="two point on the licence and a 150$ fine",
                         points=2, owner=owner_3)

    offense_4 = Offenses(type="speeding",
                         description=("Drove under influence"),
                         penalty="Eight point on the licence and a 1150$ fine",
                         points=8, owner=owner_3)
    offense_3.save()
    offense_4.save()

    car_3 = Car(color='Purple',
                type='Sedan',
                fuel_type='Petrol',
                registration='2f34-0-3f33',
                power=400,
                transmission='automatic',
                make='Mercedes',
                model='c63',
                number_of_seats='5',
                engine_cubic_capacity='4000cc',
                emission_class='EUR 6',
                fuel_consumption=11,
                production_date=datetime.date(2021, 1, 1),
                owner=owner_3
                )
    car_3.save()

    ######################################################################

    owner_4 = Owner(first_name="Lyra",
                    last_name="Ash",
                    dob=datetime.date(1981, 11, 11),
                    gender="Female")
    owner_4.save()

    dr_4 = DrivingRecords(points=0,
                          valid_driving_licence=True,
                          number_of_accidents=0,
                          owner=owner_4)
    dr_4.save()

    offense_5 = Offenses(type="wrong parking",
                         description=("Car not parked properly"),
                         penalty="50$ fine",
                         points=0, owner=owner_4)
    offense_5.save()

    car = Car(color='Black',
              type='Sedan',
              fuel_type='Petrol',
              registration='234-0-33fw3',
              power=300,
              transmission='automatic',
              make='BMW',
              model='m3',
              number_of_seats='5',
              engine_cubic_capacity='3000cc',
              emission_class='EUR 6',
              fuel_consumption=9,
              production_date=datetime.date(2020, 1, 1),
              owner=owner_1
              )
    car.save()

    ######################################################################

    owner_5 = Owner(first_name="Bob",
                    last_name="Blackwood",
                    dob=datetime.date(1978, 11, 10),
                    gender="Male")
    owner_5.save()

    dr_5 = DrivingRecords(points=0,
                          valid_driving_licence=True,
                          number_of_accidents=0,
                          owner=owner_5)
    dr_5.save()

    offense_6 = Offenses(type="day lights were off",
                         description=("day lights were not turned on, gave him a warning"),
                         penalty="Warning",
                         points=0, owner=owner_5)
    offense_6.save()

    car = Car(color='Red',
              type='SUV',
              fuel_type='Petrol',
              registration='2e34-0-333',
              power=300,
              transmission='automatic',
              make='Toyota',
              model='Land Cruiser',
              number_of_seats='7',
              engine_cubic_capacity='4600cc',
              emission_class='EUR 6',
              fuel_consumption=17,
              production_date=datetime.date(2021, 1, 1),
              owner=owner_5
              )
    car.save()

    return HttpResponse("<h1>DONE</h1>")


#having data in our database, we want to create a few more view functions to query it
@require_http_methods(["GET"])
def get_all(request):
    driving_records = DrivingRecords.objects.all()

    context = {
        "driving_records": driving_records,
    }

    return render(request, "records.html", context)


#our second requirement: showing only drivers who have a valid driving licence
@require_http_methods(["GET"])
def get_with_valid_driving_licence(request):
    queryset = DrivingRecords.objects.filter(valid_driving_licence=True)

    context = {
        "driving_records": queryset
    }

    return render(request, "records.html", context)

#For our third view, we want to get all the drivers with offenses
@require_http_methods(["GET"])
def get_drivers_with_offenses(request):
    queryset = DrivingRecords.objects.filter(points__gte=1)

    context = {
        "driving_records": queryset
    }

    return render(request, "records.html", context)

#Finally, we will display cars and their owners
@require_http_methods(["GET"])
def get_cars_and_their_owners(request):
    queryset = Car.objects.all()

    context = {
        "cars": queryset
    }

    return render(request, "records_cars.html", context)

