# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_manager', '0005_job_thread_count'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='thread_count',
            new_name='model_name',
        ),
    ]
