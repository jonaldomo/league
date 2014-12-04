# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='athletes',
            field=models.ManyToManyField(to='teams.Athlete'),
            preserve_default=True,
        ),
    ]
