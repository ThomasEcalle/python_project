# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-22 19:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_node'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='final_node',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='website.Node'),
        ),
    ]