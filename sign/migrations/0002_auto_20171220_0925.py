# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-12-20 01:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sign', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='guest',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='guest',
            name='event',
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.DateField(verbose_name='events time'),
        ),
        migrations.DeleteModel(
            name='Guest',
        ),
    ]
