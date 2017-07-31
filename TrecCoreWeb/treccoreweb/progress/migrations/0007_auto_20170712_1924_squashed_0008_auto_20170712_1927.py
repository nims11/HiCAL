# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-12 22:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('progress', '0007_auto_20170712_1924'), ('progress', '0008_auto_20170712_1927')]

    dependencies = [
        ('progress', '0006_auto_20170708_1942'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='timespent',
        ),
        migrations.AddField(
            model_name='task',
            name='timespent',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='task',
            name='last_activity',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]