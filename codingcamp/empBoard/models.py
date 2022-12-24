from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User
from cataloge.models import Training

class Messages(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE, null=True)
    result = models.CharField(verbose_name="result", max_length=50,default="accepted")
    training_name = models.CharField(max_length=200)
    content_url = models.URLField(verbose_name="url" ,max_length=200)
    def __str__(self):
        return f'{self.user} request was {self.result}'

class UserTrainings(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    training = models.ForeignKey(Training, on_delete=CASCADE)
    status = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.user}-> {self.training}'