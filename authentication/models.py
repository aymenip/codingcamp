from django.db import models
from django.db.models.fields import CharField, EmailField

class EmployeeRegisterRequest(models.Model):
    first_name = models.CharField(max_length=50 , verbose_name="First name")
    last_name = models.CharField(max_length=50 , verbose_name="Last name")
    username = models.CharField(max_length=100, verbose_name="Username", unique=True)
    email = models.EmailField(verbose_name="Email")
    password = models.CharField(max_length=100, verbose_name="Password")
    birthday = models.DateField(verbose_name="Birthday")
    created = models.DateField(auto_now_add=True)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
