from django.db import models
from django_countries.fields import CountryField

class JobApplication(models.Model):
    full_name = models.CharField(max_length=50, null=False, blank=False)
    job_choices = [
        ("Store Manager", "Store Manager"),
        ("Sales Manager", "Sales Manager"),
        ("Delivery Driver", "Delivery Driver"),
        ("Delivery Driver (International)", "Delivery Driver (International)"),
    ]
    job = models.CharField(choices=job_choices, null=True, blank=False, max_length=50)
    email = models.EmailField(max_length=254, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)

    def __str__(self):
        return self.full_name
