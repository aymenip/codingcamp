from django import forms
from django.forms import ModelForm
from .models import EmployeeRegisterRequest


class EmployeeRegisterRequestForm(ModelForm):
    class Meta:
        model = EmployeeRegisterRequest
        fields = '__all__'
        widgets = {'password': forms.PasswordInput()}