from django.contrib import admin

# Register your models here.
from .models import Employee, Supervisor, Workday, Workweek

admin.site.register(Employee)
admin.site.register(Supervisor)
admin.site.register(Workday)
admin.site.register(Workweek)