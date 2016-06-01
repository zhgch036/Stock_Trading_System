#coding:utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class SecurityAccountInfo(models.Model):
    SecurityID = models.CharField(max_length=20)


class UserTable(models.Model):
    UserID = models.CharField(max_length=20)
    Name = models.CharField(max_length=20)
    IDcard = models.CharField(max_length=20)
    Gender = models.IntegerField()
    Occupation = models.CharField(max_length=20)
    EduInfo = models.CharField(max_length=20)
    HomeAddr = models.TextField(max_length=20)
    Department = models.TextField(max_length=20)
    Tel = models.CharField(max_length=20)
    MailAddr = models.CharField(max_length=20)
    Age = models.IntegerField()


class CapitalAccountInfo(models.Model):
    AccountID = models.CharField(max_length=20)
    Password = models.CharField(max_length=20)
    Isfirst = models.BooleanField(default=1)
    UserTable = models.ForeignKey(UserTable)
    BuyPassword = models.CharField(max_length=20)
    SecurityAccount = models.ForeignKey(SecurityAccountInfo)
    loginPwdWrongNum = models.IntegerField(default=0)
    transPwdWrongNum = models.IntegerField(default=0)
    lastTimeTrans = models.DateTimeField(max_length=20)
    lastTimeLogin = models.DateTimeField(max_length=20)
    IsTransFreeze = models.BooleanField(max_length=20)
    IsLoginFreeze = models.BooleanField(max_length=20)
