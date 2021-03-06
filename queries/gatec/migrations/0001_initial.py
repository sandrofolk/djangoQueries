# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-06 21:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fardao',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('empresa', models.IntegerField()),
                ('safra', models.IntegerField()),
                ('peso', models.DecimalField(decimal_places=2, max_digits=15)),
                ('status', models.IntegerField()),
            ],
            options={
                'verbose_name': 'fardão',
                'verbose_name_plural': 'fardões',
            },
        ),
        migrations.CreateModel(
            name='Pluma',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('empresa', models.IntegerField()),
                ('safra', models.IntegerField()),
                ('peso', models.DecimalField(decimal_places=2, max_digits=15)),
                ('status', models.DecimalField(decimal_places=1, max_digits=2)),
                ('fardao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gatec.Fardao')),
            ],
        ),
    ]
