# Generated by Django 4.0 on 2021-12-30 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cataloge', '0002_remove_training_name_training_content_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='training',
            name='content',
            field=models.FileField(max_length=255, null=True, upload_to='documents/%Y/%m/%d', verbose_name='Content'),
        ),
    ]