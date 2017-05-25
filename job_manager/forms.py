from django import forms

from .models import Job


class JobForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    #file_first = forms.FileField(label='Select a file')
    #file_second = forms.FileField(label='Select a file')
    #file_third = forms.FileField(label='Select a file')
    #file_forth = forms.FileField(label='Select a file')
    #email = forms.EmailField(label="Email Address")

    class Meta:
        model = Job
        # fields = ['file_first', 'file_second', 'file_third', 'file_forth', 'email', 'hostname', 'username', 'password']
        fields = ['file_first', 'file_second', 'experiment_name','model_name','cluster_number', 'email', 'hostname', 'username', 'password']