# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2020-06-06 07:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cities_light', '0006_compensate_for_0003_bytestring_bug'),
        ('community', '0015_merge_20200404_0832'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='location',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='cities_light.City', verbose_name='Location'),
        ),
        migrations.AddField(
            model_name='requestcommunity',
            name='location',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='cities_light.City', verbose_name='Location'),
        ),
    ]
