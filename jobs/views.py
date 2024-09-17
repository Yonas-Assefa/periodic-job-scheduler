from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from .forms import JobForm, ScriptForm, ScriptFormSet
from .models import Job, Script

# Create your views here.


def job_view_test(request):
    return render(request, 'jobs/base.html')

def job_view_test2(request):
    return render(request, 'jobs/header.html')

from django.shortcuts import render, redirect
from .forms import JobForm, ScriptFormSet
from .models import Script

def add_job(request):
    if request.method == 'POST':
        
        job_form = JobForm(request.POST)
        script_formset = ScriptFormSet(request.POST, prefix='script_formset')


        if job_form.is_valid() and script_formset.is_valid():
            job = job_form.save()
            scripts = script_formset.save(commit=False)
            for script in scripts:
                script.job = job
                script.save()
            return redirect('/jobs/base.html')
        else:
            pass
    else:
        job_form = JobForm()
        script_formset = ScriptFormSet(prefix='script_formset')

    return render(request, 'jobs/add_job.html', {
        'job_form': job_form,
        'script_formset': script_formset,
    })
