# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-08 22:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0017_auto_20161005_0058'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='code_prod',
            field=models.CharField(blank=True, max_length=70, verbose_name='Code Produit'),
        ),
    ]
