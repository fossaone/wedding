# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AmyAndNick', '0002_auto_20141107_2149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guest',
            name='date',
        ),
        migrations.RemoveField(
            model_name='guest',
            name='paid',
        ),
    ]
