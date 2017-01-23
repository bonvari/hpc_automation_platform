# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_manager', '0003_job_latest_run'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='experiment_name',
            field=models.CharField(default='exp', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='job',
            name='file_first',
            field=models.FileField(verbose_name='Model', upload_to='uploads/%Y_%m_%d/'),
        ),
        migrations.AlterField(
            model_name='job',
            name='file_second',
            field=models.FileField(verbose_name='Experiment', upload_to='uploads/%Y_%m_%d/'),
        ),
    ]
