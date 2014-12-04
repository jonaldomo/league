# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0004_league_organization'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('home_score', models.PositiveIntegerField()),
                ('away_score', models.PositiveIntegerField()),
                ('away_team', models.ForeignKey(related_name='+', to='teams.Team')),
                ('home_team', models.ForeignKey(related_name='+', to='teams.Team')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
