# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('email_address', models.EmailField(max_length=75)),
                ('date', models.DateField(auto_now=True)),
                ('spouse', models.CharField(max_length=128)),
                ('children', models.IntegerField()),
                ('babies', models.IntegerField()),
                ('rehersal_dinner', models.BooleanField()),
                ('wedding', models.BooleanField()),
                ('stay_in_cabin', models.BooleanField()),
                ('vegetarian', models.BooleanField()),
                ('notes', models.CharField(max_length=256)),
                ('paid', models.BooleanField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
