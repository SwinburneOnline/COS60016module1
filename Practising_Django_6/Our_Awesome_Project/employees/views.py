#from django.shortcuts import render
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from .models import StaffInfo, Role
from django.http import HttpResponse

# Create your views here.


@require_http_methods(["GET"])
def populate_with_sample_data(request):
    employee_1 = StaffInfo(name="Lauren", last_name="Ash", age=21, gender="Female")
    employee_1.save()

    employee_2 = StaffInfo(name="John", last_name="Doe", age=30, gender="male")
    employee_2.save()

    employee_3 = StaffInfo(name="Stanly", last_name="Pit", age=21, gender="Male")
    employee_3.save()

    employee_4 = StaffInfo(name="Lyra", last_name="storm", age=25, gender="Female")
    employee_4.save()

    employee_5 = StaffInfo(name="Ana", last_name="Cloud", age=33, gender="Female")
    employee_5.save()

    role_1 = Role(role="Accountant", location="New York", staff=employee_1)
    role_1.save()

    role_2 = Role(role="Driver", location="Austin", staff=employee_2)
    role_2.save()

    role_3 = Role(role="Security", location="Palo Alto", staff=employee_3)
    role_3.save()

    role_4 = Role(role="Driver", location="New York", staff=employee_4)
    role_4.save()

    role_5 = Role(role="Receptionist", location="New York", staff=employee_5)
    role_5.save()

    return HttpResponse("<h1>DONE</h1>")


@require_http_methods(["GET"])
def show_all(request):
    queryset = Role.objects.all()

    return render(request, "employees.html", {"queryset": queryset})


@require_http_methods(["GET"])
def order_by_location(request):
    queryset = Role.objects.order_by('location')

    return render(request, 'employees.html', {'queryset': queryset})


@require_http_methods(["GET"])
def order_by_role(request):
    queryset = Role.objects.order_by('role')

    return render(request, 'employees.html', {'queryset': queryset})