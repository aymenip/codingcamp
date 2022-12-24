from django import forms
from django.forms import ModelForm
from .models import Organization, Training


class OrganizationForm(ModelForm):
    class Meta:
        model = Organization
        fields = '__all__'

class TrainingForm(ModelForm):
    class Meta:
        model = Organization
        fields = '__all__'