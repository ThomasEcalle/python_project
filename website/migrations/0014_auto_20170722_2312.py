# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-22 21:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_auto_20170722_2125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tournament',
            name='final_node',
        ),
        migrations.AddField(
            model_name='node',
            name='tournament',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='website.Tournament'),
            preserve_default=False,
        ),
    ]
