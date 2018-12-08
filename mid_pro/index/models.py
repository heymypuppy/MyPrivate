from django.db import models

# Create your models here.

class shop_brand(models.Model):

    shop_addr = models.CharField(max_length=100)

    image_addr = models.CharField(max_length=100)

    shop_name = models.CharField(max_length=50)

    shop_lever = models.CharField(max_length=50)

    is_working = models.BooleanField(default=True)

class addr_handler(models.Model):
    recv_name = models.CharField(max_length=10)

    recv_tel = models.CharField(max_length=11)

    recv_addr = models.CharField(max_length=30)

    basic_tel = models.CharField(max_length=20)




class orderInfo(models.Model):
    basicTel = models.CharField(max_length=11)

    orderNum = models.CharField(max_length=20)

    date = models.DateTimeField(max_length=20)

    orderImg = models.CharField(max_length=100)

    resName = models.CharField(max_length=15)

    orderType = models.CharField(max_length=20)

    orderStatus = models.CharField(max_length=20)

    orderAcount = models.CharField(max_length=10)

    restTel = models.CharField(max_length=20)

class collect(models.Model):
    basicTel = models.CharField(max_length=20)

    resName = models.CharField(max_length=20)

    resType = models.CharField(max_length=20)

    resLevel = models.CharField(max_length=20)

    resImg = models.CharField(max_length=100)

    collect_status = models.CharField(max_length=30)