from django.db import models

class Contact(models.Model):
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    description = models.TextField()

    def __str__(self):
        return self.full_name

    def get_friendly_name(self):
        return self.email
