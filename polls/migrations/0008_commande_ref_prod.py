# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-15 05:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20160915_0722'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='ref_prod',
            field=models.ManyToManyField(to='polls.Produit'),
        ),
    ]
