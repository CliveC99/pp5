from django.http import HttpResponse

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
        return HttpResponse(
            content=f'Webhook recived: {event["type"]}',
            status=200)
    
    def handle_payment_intent_failed(self, event):
        """ Handle payment intend failed from stripe """
        return HttpResponse(
            content=f'Webhook recived: {event["type"]}',
            status=200)
