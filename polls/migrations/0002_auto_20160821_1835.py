# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-21 16:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorie',
            name='url_categorie',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produit',
            name='remise_prod',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='produit',
            name='image_prod',
            field=models.ImageField(upload_to='polls/static/polls/images'),
        ),
    ]