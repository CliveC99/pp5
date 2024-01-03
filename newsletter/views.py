from django.shortcuts import render, redirect, reverse
from .forms import NewsletterForm
from django.contrib import messages


def newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST, request.FILES)
        if form.is_valid():
            newsletter = form.save()
            messages.success(request, 'Thanks for subscribing!')
            return redirect(reverse('newsletter'))
        else:
            messages.error(request,
                           ('Failed to subscribe to the newsletter, try again!'))
    else:
        newsletter_form = NewsletterForm()

    template = 'newsletter/newsletter.html'
    context = {
        'newsletter_form': newsletter_form,
    }

    return render(request, template, context)