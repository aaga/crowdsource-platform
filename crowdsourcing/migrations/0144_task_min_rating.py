# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-07 06:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crowdsourcing', '0143_auto_20160905_0307'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='min_rating',
            field=models.FloatField(default=3.0),
        ),
    ]
