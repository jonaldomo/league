# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0003_organization'),
    ]

    operations = [
        migrations.AddField(
            model_name='league',
            name='organization',
            field=models.ForeignKey(default=1, to='teams.Organization'),
            preserve_default=False,
        ),
    ]
