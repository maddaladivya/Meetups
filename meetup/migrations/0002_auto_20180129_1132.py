# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-29 11:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pastevents',
            name='comment',
            field=models.CharField(default=False, max_length=10000),
        ),
    ]
