# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-05-21 16:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0010_auto_20200521_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='author',
            field=models.CharField(blank=True, default='', max_length=150),
        ),
    ]
