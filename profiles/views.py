from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order

@login_required
def profile(request):
    """ Display a users profile """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated!')
        else:
            messages.error(request, 'Failed to update profile, check the form and try again.')
    else:
        form = UserProfileForm(instance=profile)


    template = 'profiles/profile.html'
    context = {
        'form': form,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_history):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, f'This is an old conformation for {order_number}. An email was sent on the order date.')

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)