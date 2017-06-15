# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-06-15 19:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('silo', '0013_deletedsilos'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormulaFieldMapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mapping', models.TextField()),
                ('operation', models.TextField()),
                ('silo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='silo.Silo')),
            ],
        ),
    ]
