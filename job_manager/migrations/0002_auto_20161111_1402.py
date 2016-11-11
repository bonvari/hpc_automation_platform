# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('job_manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='user', editable=False),
        ),
    ]
