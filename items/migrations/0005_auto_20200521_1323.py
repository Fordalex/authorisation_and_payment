# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-05-21 13:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_auto_20200521_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='username',
            field=models.CharField(default='freeaccount', max_length=150),
        ),
    ]
