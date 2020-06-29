from django.contrib import admin

from api import models

admin.site.register(models.Employee)
admin.site.register(models.Student)
