# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-03-15 18:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sorminformation', '0003_informationasset_information_class_controls'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnvironmentObject',
            fields=[
                ('name', models.CharField(max_length=90, verbose_name='Наименование типа объекта среды')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
