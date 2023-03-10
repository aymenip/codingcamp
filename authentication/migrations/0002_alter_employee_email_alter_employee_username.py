# Generated by Django 4.0 on 2021-12-27 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='username',
            field=models.CharField(max_length=100, unique=True, verbose_name='Username'),
        ),
    ]
