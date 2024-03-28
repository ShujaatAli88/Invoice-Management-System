from django.contrib import admin
from .models import Invoice, Registration
from . forms import InvoiceForm

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ["name", "invoice_number", "invoice_date"]
    # form = InvoiceForm

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ["first_name","last_name","p_number"]

admin.site.register(Invoice,InvoiceAdmin)
admin.site.register(Registration,RegistrationAdmin)