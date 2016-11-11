# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_manager', '0002_job_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='latest_run',
            field=models.IntegerField(default=1),
        ),
    ]
