from django import forms
from django.forms import ModelForm
from .models import EmployeeRegisterRequest


class EmployeeRegisterRequestForm(ModelForm):
    class Meta:
        model = EmployeeRegisterRequest
        file_field = forms.FileField(
            widget=forms.ClearableFileInput(attrs={'multiple': False}))
        fields = '__all__'
        widgets = {'password': forms.PasswordInput()}
