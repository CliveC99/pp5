from django.shortcuts import render, redirect, reverse
from .forms import JobForm
from django.contrib import messages


def job(request):
    if request.method == 'POST':
        job = JobForm(request.POST, request.FILES)
        if form.is_valid():
            job = form.save()
            messages.success(request, 'Successfully Applied!')
            return redirect(reverse('job'))
        else:
            messages.error(request,
                           ('Failed to apply, try again!'))
    else:
        job_form = JobForm()

    template = 'job/job.html'
    context = {
        'job_form': job_form,
    }

    return render(request, template, context)

