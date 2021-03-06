# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-27 12:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CapitalAccountInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AccountID', models.CharField(max_length=20)),
                ('Password', models.CharField(max_length=20)),
                ('Isfirst', models.BooleanField(default=1)),
                ('BuyPassword', models.CharField(max_length=20)),
                ('loginPwdWrongNum', models.IntegerField(default=0)),
                ('transPwdWrongNum', models.IntegerField(default=0)),
                ('lastTimeTrans', models.DateTimeField(max_length=20)),
                ('lastTimeLogin', models.DateTimeField(max_length=20)),
                ('IsTransFreeze', models.BooleanField(max_length=20)),
                ('IsLoginFreeze', models.BooleanField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SecurityAccountInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SecurityID', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='UserTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserID', models.CharField(max_length=20)),
                ('Name', models.CharField(max_length=20)),
                ('IDcard', models.CharField(max_length=20)),
                ('Gender', models.IntegerField(max_length=20)),
                ('Occupation', models.CharField(max_length=20)),
                ('EduInfo', models.CharField(max_length=20)),
                ('HomeAddr', models.TextField(max_length=20)),
                ('Department', models.TextField(max_length=20)),
                ('Tel', models.CharField(max_length=20)),
                ('MailAddr', models.CharField(max_length=20)),
                ('Age', models.IntegerField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='capitalaccountinfo',
            name='SecurityAccount',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.SecurityAccountInfo'),
        ),
        migrations.AddField(
            model_name='capitalaccountinfo',
            name='UserTable',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.UserTable'),
        ),
    ]
