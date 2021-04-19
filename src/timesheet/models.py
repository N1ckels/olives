from django.db import models
from django.urls import reverse

# Create your models here.

class Supervisor(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)

    def __str__(self):
        return self.name
    # def get_absolute_url(self):
    #     return reverse("products:product-detail", kwargs={"id": self.id})

class Employee(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    position = models.CharField(max_length=120)
    supervisor = models.ForeignKey(Supervisor, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
    # def get_absolute_url(self):
    #     return reverse("products:product-detail", kwargs={"id": self.id})


class Workday(models.Model):
    Starttime = models.DateTimeField(auto_now=False, auto_now_add=False)
    Endtime = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return str(self.Starttime)

class Workweek(models.Model):
    Employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    EoW = models.DateField(auto_now=False, auto_now_add=False)
    Monday = models.ForeignKey(Workday, on_delete=models.SET_NULL, null=True)
    # Tuesday = models.ForeignKey(Workday, on_delete=models.SET_NULL, null=True)
    # Wednesday = models.ForeignKey(Workday, on_delete=models.SET_NULL, null=True)
    # Thursday = models.ForeignKey(Workday, on_delete=models.SET_NULL, null=True)
    # Friday = models.ForeignKey(Workday, on_delete=models.SET_NULL, null=True)
    # Saturday = models.ForeignKey(Workday, on_delete=models.SET_NULL, null=True)
    # Sunday = models.ForeignKey(Workday, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return (str(self.Employee) + " " + str(self.EoW))