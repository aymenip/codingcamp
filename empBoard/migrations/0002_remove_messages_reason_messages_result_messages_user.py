# Generated by Django 4.0 on 2021-12-30 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('empBoard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messages',
            name='reason',
        ),
        migrations.AddField(
            model_name='messages',
            name='result',
            field=models.CharField(default='accepted', max_length=50, verbose_name='result'),
        ),
        migrations.AddField(
            model_name='messages',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
