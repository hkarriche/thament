# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-16 22:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_auto_20160917_0004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commande',
            name='meth_paiemet',
        ),
        migrations.DeleteModel(
            name='methode_paiement',
        ),
    ]
