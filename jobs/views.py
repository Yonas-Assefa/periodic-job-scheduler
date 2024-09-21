from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404
from .forms import JobForm, ScriptForm, ScriptFormSet
from .models import Job, Script
from django.contrib import messages

def home(request):
    jobs = Job.objects.all().order_by('created_at')
    jobs_with_scripts = []
    for job in jobs:
        scripts = job.scripts.all()  # Use related_name to get all scripts for a job
        jobs_with_scripts.append({
            'job': job,
            'scripts': scripts,
        })

    return render(request, 'jobs/job_list.html', {
        'jobs_with_scripts': jobs_with_scripts,
    })


def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    scripts = job.scripts.all()  # Fetch all scripts associated with the job

    return render(request, 'jobs/job_detail.html', {
        'job': job,
        'scripts': scripts,
    })

def job_view_test2(request):
    return render(request, 'jobs/header.html')

def add_job(request):
    if request.method == 'POST':
        job_form = JobForm(request.POST)
        script_formset = ScriptFormSet(request.POST, prefix='script_formset')

        if job_form.is_valid() and script_formset.is_valid():
            job = job_form.save()
            scripts = script_formset.save(commit=False)

            scripts_to_save = [script for script in scripts if not script.delete_script]
            for script in scripts_to_save:
                script.job = job

            for script in scripts_to_save:
                script.save()
            Script.reorder_scripts(job.id)

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
