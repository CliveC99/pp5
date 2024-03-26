from django.http import HttpResponse

from .models import Order, OrderLineItem
from products.models import Product

import json
import time

class StripeWH_Handler:
    """ Handles stripe webhooks """
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """ Handles unexpected webhook event """
        return HttpResponse(
            content=f'Unhandled Webhook recived: {event["type"]}',
            status=200)
    
    def handle_payment_intent_succeeded(self, event):
        """ Handle payment intend succeeded from stripe """
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info

        # Get the Charge object
        stripe_charge = stripe.Charge.retrieve(
            intent.latest_charge
            )

        billing_details = stripe_charge.billing_details
        shipping_details = intent.shipping
        grand_total = round(stripe_charge.amount / 100, 2)

        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None
                
        
        order_exist = False
        attempt = 1
        while attempt <= 5:
            try:
                order= Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    grand_total=grand_total,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                order_exist = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exist:
            return HttpResponse(
                content=f'Webhook recived: {event["type"]} | SUCCESS: Verified order already in DB',
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                full_name=shipping_details.name,
                email=billing_details.email,
                grand_total=grand_total,
                original_bag=bag,
                stripe_pid=pid,
                )
                for item_id, item_data in json.loads(bag).items():
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook recived: {event["type"]} | ERROR: {e}',
                    status=500)
        return HttpResponse(
                    content=f'Webhook recived: {event["type"]} | ERROR: {e}',
                    status=500)
    
    def handle_payment_intent_failed(self, event):
        """ Handle payment intend failed from stripe """
        return HttpResponse(
            content=f'Webhook recived: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)
