# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-23 16:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20160823_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagecontact',
            name='contenu',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='messagecontact',
            name='date_msg',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='messagecontact',
            name='email',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='messagecontact',
            name='num_msg',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='messagecontact',
            name='objet',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='messagecontact',
            name='tel',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
