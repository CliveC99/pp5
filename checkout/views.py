from django.shortcuts import render, redirect, reverse


from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51O2r6OGdP1AcvpQtklyNX62v9INUosIWD4Oa01gWJjXYCOVjt8QI53CHjmHUr7FD13MxBT3zVbKnnkOp0mcWZWU8007tnBUxZb',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)