from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)

    def __str__(self):
        return self.name +' '+ self.surname


class Dependents(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    work = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    education = models.CharField(max_length=50)
    maritalStatus = models.CharField(max_length=50)
    relationship = models.CharField(max_length=50)
    employeeID = models.ForeignKey(Employee,on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.name +' '+ self.surname
