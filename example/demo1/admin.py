from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.User)
admin.site.register(models.House)
admin.site.register(models.Application)
admin.site.register(models.Customerserver)