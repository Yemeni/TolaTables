# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-06-06 16:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('silo', '0011_auto_20170207_1051'),
    ]

    operations = [
        migrations.AddField(
            model_name='thirdpartytokens',
            name='username',
            field=models.CharField(max_length=60, null=True),
        ),
    ]
