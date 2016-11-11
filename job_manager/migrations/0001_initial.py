# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import job_manager.models
from django.conf import settings
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ClusterAccount',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('host', models.CharField(max_length=100, verbose_name='host')),
                ('username', models.CharField(max_length=100, verbose_name='username')),
                ('password', models.CharField(max_length=100, verbose_name='password')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('user', models.ForeignKey(verbose_name='user', editable=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'cluster account',
                'verbose_name_plural': 'cluster accounts',
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('model_file', models.FileField(verbose_name='model file', upload_to=job_manager.models.get_upload_path)),
                ('experiment_file', models.FileField(verbose_name='experiment file', upload_to=job_manager.models.get_upload_path)),
                ('add_date', models.DateTimeField(verbose_name='add date', auto_now_add=True)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'job',
                'verbose_name_plural': 'jobs',
            },
        ),
        migrations.CreateModel(
            name='JobResult',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('key', models.UUIDField(verbose_name='key', default=uuid.uuid1)),
                ('start_time', models.DateTimeField(verbose_name='start', auto_now_add=True)),
                ('result', models.TextField(verbose_name='result')),
                ('cluster', models.ForeignKey(to='job_manager.ClusterAccount', verbose_name='cluster')),
                ('job', models.ForeignKey(to='job_manager.Job', verbose_name='job')),
            ],
            options={
                'verbose_name': 'job result',
                'verbose_name_plural': 'job results',
            },
        ),
    ]
