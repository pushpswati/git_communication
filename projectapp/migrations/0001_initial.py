# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-03 09:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('username', models.CharField(blank=True, default=b'', max_length=100)),
                ('password', models.CharField(blank=True, default=b'', max_length=10)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
