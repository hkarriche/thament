# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-28 09:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_auto_20160926_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='owner',
            field=models.CharField(blank=True, default='', max_length=70, verbose_name='Proprietaire'),
        ),
    ]
