# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-05-21 16:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0009_auto_20200521_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='author',
            field=models.CharField(default=None, max_length=150),
        ),
    ]
