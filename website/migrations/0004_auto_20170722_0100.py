# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-21 23:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_touurnament'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Touurnament',
            new_name='Tournament',
        ),
    ]
