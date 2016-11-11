from django.contrib import admin

from .models import ClusterAccount, Job, JobResult


class ClusterAccountAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'host', 'username']
    list_filter = ['user', 'host', 'username']
    search_fields = ['user__username', 'title', 'host', 'username']

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(ClusterAccountAdmin, self).save_model(request, obj, form, change)


class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'model_file', 'experiment_file', 'add_date']
    list_filter = ['owner']
    search_fields = ['owner__username', 'title']
    date_hierarchy = 'add_date'

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        super(JobAdmin, self).save_model(request, obj, form, change)


class JobResultAdmin(admin.ModelAdmin):
    list_display = ['job', 'cluster', 'key', 'start_time']
    list_filter = ['job', 'cluster', 'job__owner']
    search_fields = ['job__title', 'cluster__title']
    date_hierarchy = 'start_time'


admin.site.register(ClusterAccount, ClusterAccountAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(JobResult, JobResultAdmin)