# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-18 10:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crowdsourcing', '0070_auto_20160218_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='crowdsourcing.City'),
        ),
        migrations.AlterField(
            model_name='address',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='crowdsourcing.Country'),
        ),
    ]
