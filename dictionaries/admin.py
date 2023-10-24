from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Dictionary)
admin.site.register(models.Term)