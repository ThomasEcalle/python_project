# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-22 12:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20170722_1349'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Player')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Tournament')),
            ],
        ),
        migrations.AddField(
            model_name='tournament',
            name='players',
            field=models.ManyToManyField(through='website.Participation', to='website.Player'),
        ),
    ]
