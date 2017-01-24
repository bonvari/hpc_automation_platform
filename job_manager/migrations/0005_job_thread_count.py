# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_manager', '0004_auto_20170123_1824'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='thread_count',
            field=models.CharField(max_length=10, default=1),
            preserve_default=False,
        ),
    ]
