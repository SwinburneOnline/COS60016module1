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



#what's this?
"""
offenses = Offenses.objects.all()
context = {
    "offenses": offenses,
    "driver_records": driver_records,
    "owner": owner,
    "car": car,
}

return render(request, <We need a template here>, context=context)

"""


