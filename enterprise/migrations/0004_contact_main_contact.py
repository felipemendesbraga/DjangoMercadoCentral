# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-13 05:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise', '0003_auto_20160913_0426'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='main_contact',
            field=models.BooleanField(default=True),
        ),
    ]
