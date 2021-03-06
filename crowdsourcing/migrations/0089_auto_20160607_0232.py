# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-07 02:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crowdsourcing', '0088_emailnotification'),
    ]

    operations = [
        migrations.RenameField(
            model_name='messagerecipient',
            old_name='user',
            new_name='recipient',
        ),
        migrations.AlterField(
            model_name='emailnotification',
            name='recipient',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
