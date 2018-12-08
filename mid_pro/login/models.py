from django.db import models

# Create your models here.

class msg_veri(models.Model):
    #id列，自增，主键
    #电话号码，验证码
    Tel = models.CharField(max_length=11)

    ver = models.CharField(max_length=5)

class UserInfo(models.Model):

    #用户手机，密码

    tel = models.CharField(max_length=11)

    pwd = models.CharField(max_length=12)
