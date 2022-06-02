from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Employee,Dependents

# Create your views here.

def show_all_emps(request):
    employees = Employee.objects.all()
    emp = serializers.serialize('json',employees)
    return render(request,'Dependent/main.html',{'emp':emp})

def show_dependent(request,id):
    emp = Employee.objects.get(id=id)
    dependents = Dependents.objects.filter(employeeID = emp)
    return render(request,'Dependent/index2.html',{'dependents':dependents,'id':id})


# -------------------------------------------------
# -------------------------------------------------

def updateDependent(request):
    if request.method == 'POST':
        # updateData(request)
        dependentID = request.POST.get('dependentID')
        employeeID = request.POST.get('employeeID')
        relationship = request.POST.get('relationship')
        Name = request.POST.get('employeeName')
        surname = request.POST.get('surname')
        gender = request.POST.get('gender')
        Work = request.POST.get('Work')
        Age = request.POST.get('Age')
        education = request.POST.get('education')
        marital_status = request.POST.get('marital_status')

        # fetch current dependent 
        currentDependent = Dependents.objects.get(id=dependentID)
        currentDependent.name = Name
        currentDependent.surname = surname
        currentDependent.gender = gender
        currentDependent.work = Work
        currentDependent.age = Age
        currentDependent.education = education
        currentDependent.maritalStatus = marital_status
        currentDependent.relationship = relationship
        currentDependent.save()

        return redirect('allDependent',employeeID)     # for redirect to 'name =' main page without reposting data

def insertDependent(request):
    if request.method == 'POST':
        employeeID = request.POST.get('employeeID')
        relationship = request.POST.get('relationship')
        Name = request.POST.get('employeeName')
        surname = request.POST.get('surname')
        gender = request.POST.get('gender')
        Work = request.POST.get('Work')
        Age = request.POST.get('Age')
        education = request.POST.get('education')
        marital_status = request.POST.get('marital_status')
        # -----------
        employee = Employee.objects.get(id=employeeID)
        print(employee)
        # fetch current dependent 
        currentDependent = Dependents()
        currentDependent.employeeID = employee
        currentDependent.name = Name
        currentDependent.surname = surname
        currentDependent.gender = gender
        currentDependent.work = Work
        currentDependent.age = Age
        currentDependent.education = education
        currentDependent.maritalStatus = marital_status
        currentDependent.relationship = relationship
        currentDependent.save()
        return HttpResponse(1)


def deleteDependent(request):
    if request.method == 'POST':
        # updateData(request)
        dependentID = request.POST.get('dependentID')
        # fetch current dependent 
        currentDependent = Dependents.objects.get(id=dependentID)
        currentDependent.delete()
        return HttpResponse(1)
