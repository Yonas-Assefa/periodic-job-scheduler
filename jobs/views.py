from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from .forms import JobForm, ScriptForm, ScriptFormSet

# Create your views here.


def job_view_test(request):
    return render(request, 'jobs/base.html')

def job_view_test2(request):
    return render(request, 'jobs/header.html')

def add_job(request):
   
    job_form = JobForm(request.POST or None)
    script_form = ScriptForm(request.POST or None)
    
   
    if request.method == 'POST':
        if job_form.is_valid() and script_form.is_valid():
           
            job = job_form.save(commit=False)
            script = script_form.cleaned_data['script_content']           
            job.script = script  
            job.save()

            
            return redirect('success_page')  # Redirect to the desired page after submission

    # Render the template with both forms
    return render(request, 'jobs/add_job.html', {
        'job_form': job_form,
        'script_form': script_form
    })