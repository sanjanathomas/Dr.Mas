# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-03-07 20:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mas', '0005_auto_20180307_2126'),
    ]

    operations = [
        migrations.CreateModel(
            name='disease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('did', models.IntegerField()),
                ('diagnose', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='diseases',
        ),
    ]
