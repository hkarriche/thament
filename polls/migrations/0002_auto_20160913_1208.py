# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-13 10:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commande',
            name='ref_prod',
        ),
        migrations.AddField(
            model_name='produit',
            name='commande',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Commande'),
        ),
    ]