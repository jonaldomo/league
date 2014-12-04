# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0006_game_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='slug',
            field=models.SlugField(default='blah'),
            preserve_default=False,
        ),
    ]
