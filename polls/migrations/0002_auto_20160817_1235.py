# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-17 10:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'ordering': ['-modified'], 'verbose_name_plural': 'Clients'},
        ),
    ]