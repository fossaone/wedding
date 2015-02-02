# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AmyAndNick', '0005_remove_guest_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guest',
            name='babies',
        ),
        migrations.RemoveField(
            model_name='guest',
            name='children',
        ),
        migrations.RemoveField(
            model_name='guest',
            name='vegetarian',
        ),
        migrations.AddField(
            model_name='guest',
            name='brunch',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
