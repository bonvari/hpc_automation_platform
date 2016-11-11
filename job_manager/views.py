from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from django.contrib.messages import add_message, get_messages

from .forms import JobForm
from .models import Job
import os
from . import commands
from .split_nlogo_experiment import spliter


class JobDeleteView(DeleteView):
    model = Job
    success_url = reverse_lazy('job-list')


def run(request, id):
    data = Job.objects.get(pk=id)
    #os.system("cat %s" % data.file_first.path)
    try:
        data.state = True
            # spliter(data.file_first.path, "experiment1", os.path.dirname(data.file_first.path))
            # data.result = commands.run_command(data.hostname, data.username, data.password)
            # data.state = False
        data.result = commands.submit_job(data, data.hostname, data.username, data.password)
        data.save()
    except Exception as error:
        #add_message
        print(error)
        print("error: invalid nlogo file")
    return redirect('job-list')


def stop(request,id):
    data = Job.objects.get(pk=id)
    data.state = False
    data.save()
    return redirect('job-list')


def upload_job_view(request):
    if request.method == "POST":
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            #instance = Job(file_first=request.FILES['file_first'], file_second=request.FILES['file_second'],
             #              file_third=request.FILES.get('file_third', None), file_forth=request.FILES.get('file_forth', None),
             #              email=request.POST['email'])
            #instance.save()
            form.save()
            return HttpResponseRedirect('/')
        else:
            return render(request, 'job_manager/job_upload.html', {'form': form})
    else:
        form = JobForm()
        return render(request, 'job_manager/job_upload.html', {'form': form})


class JobListView(ListView):
    model = Job

    #def get_context_data(self, **kwargs):
     #   d = super(JobListView, self).get_context_data(**kwargs)
      #  d.update(errormsg=get_messages())

