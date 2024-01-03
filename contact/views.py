from django.shortcuts import render, redirect, reverse
from .forms import ContactForm
from django.contrib import messages


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            contact = form.save()
            messages.success(request, 'Successfully Contacted!')
            return redirect(reverse('contact'))
        else:
            messages.error(request,
                           ('Failed to contact the page, try again!'))
    else:
        contact_form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'contact_form': contact_form,
    }

    return render(request, template, context)

