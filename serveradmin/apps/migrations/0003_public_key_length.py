# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-20 11:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_public_key_support'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publickey',
            name='key_base64',
            field=models.CharField(max_length=2048, primary_key=True, serialize=False),
        ),
    ]
