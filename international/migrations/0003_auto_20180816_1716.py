# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-08-16 17:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('international', '0002_auto_20180816_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='shipper_country',
            field=models.CharField(max_length=3, verbose_name='shipper_country'),
        ),
    ]