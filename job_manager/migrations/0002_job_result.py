# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='result',
            field=models.TextField(blank=True),
        ),
    ]
