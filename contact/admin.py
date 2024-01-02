from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    fields = ('full_name', 'email', 'description',)

admin.site.register(Contact, ContactAdmin)
