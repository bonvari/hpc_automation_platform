# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('file_first', models.FileField(upload_to='uploads/%Y_%m_%d/')),
                ('file_second', models.FileField(upload_to='uploads/%Y_%m_%d/')),
                ('file_third', models.FileField(upload_to='uploads/%Y_%m_%d/', blank=True)),
                ('file_forth', models.FileField(upload_to='uploads/%Y_%m_%d/', blank=True)),
                ('email', models.EmailField(max_length=254)),
                ('hostname', models.CharField(max_length=100, default='aoclsb.uab.cat')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('state', models.BooleanField(default=False)),
            ],
        ),
    ]
