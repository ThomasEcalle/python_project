# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-22 10:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_player_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='website.Group'),
            preserve_default=False,
        ),
    ]
