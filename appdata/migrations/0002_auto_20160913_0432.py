# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-13 04:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appdata', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='type',
            field=models.IntegerField(choices=[
                (0, 'Lista de produtos'),
                (1, 'P\xe1gina est\xe1tica'),
                (2, 'Contato')
            ],default=1),
        ),
        migrations.AlterField(
            model_name='section',
            name='icon',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
