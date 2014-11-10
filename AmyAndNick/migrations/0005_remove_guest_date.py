# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AmyAndNick', '0004_auto_20141109_2143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guest',
            name='date',
        ),
    ]
