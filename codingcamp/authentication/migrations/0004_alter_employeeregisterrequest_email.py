# Generated by Django 4.0 on 2021-12-30 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_rename_employee_employeeregisterrequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeregisterrequest',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
    ]
