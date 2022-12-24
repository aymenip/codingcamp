from django.contrib import admin
from .models import Organization, Training, TrainingRequest
# Register your models here.

admin.site.register(Organization)
admin.site.register(Training)
admin.site.register(TrainingRequest)