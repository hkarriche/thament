# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-03 20:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20160903_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='image_prod',
            field=models.ImageField(blank=True, upload_to=b'', verbose_name='Image'),
        ),
    ]