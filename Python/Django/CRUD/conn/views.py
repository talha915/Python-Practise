from django.shortcuts import render, redirect
from conn.models import Employees
from conn.serializers import EmployeesSerializer

# Create your views here.
def show(request):
    emps = Employees.objects.all()
    # print("Emps: ...............................................", emps)
    # return render(request,"show.html",{'employees': emps})
    serializer_class = EmployeesSerializer
    queryset = Employees.objects.all()