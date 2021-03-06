# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-14 15:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appdata', '0013_auto_20160914_0759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='icon',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='\xedcone'),
        ),
        migrations.AlterField(
            model_name='section',
            name='reference',
            field=models.CharField(max_length=20, verbose_name='refer\xeancia'),
        ),
        migrations.AlterField(
            model_name='section',
            name='title',
            field=models.CharField(max_length=50, verbose_name='t\xedtulo'),
        ),
        migrations.AlterField(
            model_name='section',
            name='type',
            field=models.IntegerField(
                choices=[
                    (0, 'Lista de produtos'),
                    (1, 'P\xe1gina est\xe1tica'),
                    (2, 'Contato')
                ],
                default=1,
                verbose_name='tipo'
            ),
        ),
    ]
