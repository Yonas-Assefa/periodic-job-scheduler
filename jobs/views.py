
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from .forms import JobForm, ScriptForm, ScriptFormSet
from .models import Job, Script
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, 'jobs/base.html')

def job_view_test2(request):
    return render(request, 'jobs/header.html')

def add_job(request):
    if request.method == 'POST':
        job_form = JobForm(request.POST)
        script_formset = ScriptFormSet(request.POST, prefix='script_formset')

        if job_form.is_valid() and script_formset.is_valid():
            job = job_form.save() 
            scripts = script_formset.save(commit=False)  

            for script in scripts:
                script.job = job

            print(scripts, job, script_formset, request.POST)
            Script.reorder_scripts(job.id)
            for script in scripts:
                script.save()
          
            messages.success(request, "Job added successfully.")
            return redirect('/')
        else:
            messages.error(request, 'There was an error creating the job.')
            return render(request, 'jobs/add_job.html', {
                'job_form': job_form,
                'script_formset': script_formset,
            })
    else:
        job_form = JobForm()
        script_formset = ScriptFormSet(prefix='script_formset')

    return render(request, 'jobs/add_job.html', {
        'job_form': job_form,
        'script_formset': script_formset,
    })
