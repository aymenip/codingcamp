from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


class Organization(models.Model):
    name = models.CharField(verbose_name="Name", max_length=200)
    rate = models.FloatField(verbose_name="Rate", default=0, max_length=1)
    trainings_nb = models.IntegerField(default=0)
    created = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name

class Training(models.Model):
    title = models.CharField(verbose_name="Title", max_length=200, null=True)
    content = models.FileField(verbose_name="Content", upload_to='documents/%Y/%m/%d', max_length=255, null=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True)
    rate = models.FloatField(verbose_name="Rate", default=0, max_length=1)
    created = models.DateField(auto_now_add=True)
    requests = models.IntegerField(default=0)
    participants = models.IntegerField(default=0)
    def __str__(self):
        return self.title[:100]


class TrainingRequest(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    training = models.ForeignKey(Training, on_delete=CASCADE)
    status = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.first_name} -> {self.training}'