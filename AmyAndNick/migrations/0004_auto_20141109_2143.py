# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('AmyAndNick', '0003_auto_20141109_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='date',
            field=models.DateTimeField(default=datetime.date(2014, 11, 9), verbose_name=b'date entered'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='guest',
            name='babies',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='guest',
            name='children',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='guest',
            name='significant_other',
            field=models.CharField(max_length=128, blank=True),
        ),
    ]
