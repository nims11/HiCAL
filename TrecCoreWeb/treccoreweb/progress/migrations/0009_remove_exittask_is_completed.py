# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-13 21:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('progress', '0008_remove_exittask_task'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exittask',
            name='is_completed',
        ),
    ]
