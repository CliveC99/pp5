from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from products.models import Product


def view_bag(request):
    """
    Shows the bag page
    """
    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """
    Add  a quantity of products to the bag
    """

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)

def update_bag(request, item_id):
    """
    Updates the quantity in the bag
    """
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})
    if quantity:
        if quantity > 0:
            bag[item_id] = quantity
        else:
            del bag[item_id]
    else:
        bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))