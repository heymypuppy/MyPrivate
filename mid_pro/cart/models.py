from django.db import models

# Create your models here.
class commodity(models.Model):
    dishName = models.CharField(max_length=50)

    dishValue = models.FloatField(max_length=10)

    dishPath = models.CharField(max_length=100)

class TemCountValue(models.Model):
    basicTel = models.CharField(max_length=11)

    dishName = models.CharField(max_length=50)

    dishNum = models.IntegerField()

    dishValue = models.IntegerField()

    dishTotal = models.IntegerField()