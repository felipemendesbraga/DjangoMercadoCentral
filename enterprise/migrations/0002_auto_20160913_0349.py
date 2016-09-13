# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-13 03:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='app',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='app',
            name='code',
            field=models.CharField(max_length=100, verbose_name='c\xf3digo'),
        ),
        migrations.AlterField(
            model_name='app',
            name='logo',
            field=models.ImageField(upload_to='app_logo', verbose_name='logomarca'),
        ),
        migrations.AlterField(
            model_name='app',
            name='name',
            field=models.CharField(max_length=150, verbose_name='nome'),
        ),
        migrations.AddField(
            model_name='contact',
            name='app',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterprise.App', verbose_name='App'),
        ),
    ]