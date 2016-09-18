# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-16 22:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_auto_20160917_0048'),
        ('orders', '0005_auto_20160917_0038'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Client'),
        ),
        migrations.AddField(
            model_name='commande',
            name='meth_paiemet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.methode_paiement'),
        ),
        migrations.AlterField(
            model_name='commande',
            name='adresse_facturation',
            field=models.CharField(blank=True, default='', max_length=200, null=True, verbose_name='Adresse Facturation'),
        ),
    ]