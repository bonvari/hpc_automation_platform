import datetime
import os
from uuid import uuid1

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify


def get_upload_path(instance, filename):
    return os.path.join(
      'uploads', '%s' % instance.owner.username, datetime.datetime.now().strftime('%Y-%m-%d'), slugify(filename))


class ClusterAccount(models.Model):
    class Meta:
        verbose_name = _('cluster account')
        verbose_name_plural = _('cluster accounts')

    user = models.ForeignKey(User, editable=False, verbose_name=_('user'))
    title = models.CharField(max_length=100, verbose_name=_('title'))
    host = models.CharField(max_length=100, verbose_name=_('host'))
    username = models.CharField(max_length=100, verbose_name=_('username'))
    password = models.CharField(max_length=100, verbose_name=_('password'))
    description = models.TextField(verbose_name=_('description'), blank=True)

    def __str__(self):
        return self.title


class Job(models.Model):
    class Meta:
        verbose_name = _('job')
        verbose_name_plural = _('jobs')

    owner = models.ForeignKey(User, editable=False, verbose_name=_('user'))
    title = models.CharField(max_length=100, verbose_name=_('title'))
    model_file = models.FileField(upload_to=get_upload_path, verbose_name=_('model file'))
    experiment_file = models.FileField(upload_to=get_upload_path, verbose_name=_('experiment file'))
    add_date = models.DateTimeField(auto_now_add=True, verbose_name=_('add date'))

    def __str__(self):
        return self.title


class JobResult(models.Model):
    class Meta:
        verbose_name = _('job result')
        verbose_name_plural = _('job results')

    job = models.ForeignKey(Job, verbose_name=_('job'))
    cluster = models.ForeignKey(ClusterAccount, verbose_name=_('cluster'))
    key = models.UUIDField(default=uuid1, verbose_name=_('key'))
    start_time = models.DateTimeField(auto_now_add=True, verbose_name=_('start'))
    result = models.TextField(verbose_name=_('result'))

    def __str__(self):
        return str(_('result: %(job_title)s-%(start_time)s')) % {
            'job_title': self.job.title,
            'start_time': self.start_time
        }
