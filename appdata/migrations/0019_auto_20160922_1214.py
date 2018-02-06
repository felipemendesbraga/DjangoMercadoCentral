# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-22 12:14
from __future__ import unicode_literals

import appdata.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appdata', '0018_auto_20160921_2123'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActiveHighlight',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('appdata.highlight',),
        ),
        migrations.AddField(
            model_name='highlight',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=appdata.models.highlight_directory_path),
        ),
    ]