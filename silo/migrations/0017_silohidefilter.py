# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-06-30 18:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('silo', '0016_columnordermapping'),
    ]

    operations = [
        migrations.CreateModel(
            name='siloHideFilter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hiddenColumns', models.TextField()),
                ('hiddenRows', models.TextField()),
                ('silo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silo.Silo')),
            ],
        ),
    ]
