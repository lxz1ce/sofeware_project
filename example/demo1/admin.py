from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.User)
admin.site.register(models.House)
admin.site.register(models.Application)
admin.site.register(models.Customerserver)
admin.site.register(models.Technician)
admin.site.register(models.Repairing)
admin.site.register(models.Reporting)
admin.site.register(models.Message)
admin.site.register(models.MyMessage)