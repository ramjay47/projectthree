from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmpForm
from .models import Employee
# Create your views here.


def welcomePage(req):
    return render(req, "emp.html", {"eform": EmpForm(), "emps": Employee.objects.all()})

def saveEmployeeInfo(req):
    print('inside save emp...',req.POST)
    form = EmpForm(req.POST)
    form.save()

    return render(req, "emp.html", {"eform" : EmpForm(),"emps" : Employee.objects.all()})

def editEmployeeInfo(req,eid):
    pass

def deleteEmployeeInfo(req,eid):
    pass