# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-15 05:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20160915_0716'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('status', '-date_created'), 'verbose_name': 'Commande', 'verbose_name_plural': 'Commandes'},
        ),
    ]
