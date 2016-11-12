from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import ClusterAccountListView, JobListView


urlpatterns = [
    url(r'^$', login_required(JobListView.as_view()), name='job-list'),
    url(r'^clusters/$', login_required(ClusterAccountListView.as_view()), name='cluster-list'),
    # url(r'^upload/$', upload_job_view, name='job-upload'),
    # url(r'^job/(?P<pk>[0-9]+)/delete/$', JobDeleteView.as_view(), name='del-job'),
    # url(r'^job/(?P<id>[0-9]+)/run/$', run, name='run-job'),
    # url(r'^job/(?P<id>[0-9]+)/stop/$', stop, name='stop-job'),
]
