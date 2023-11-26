from django.contrib import admin
from .models import Discounts


class DiscountsAdmin(admin.ModelAdmin):
    list_display = ['code', 'valid_from', 'valid_to', 'discount', 'active']

admin.site.register(Discounts, DiscountsAdmin)
