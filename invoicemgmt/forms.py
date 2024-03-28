from django import forms
from . models import Invoice , Registration

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = [
            "name","invoice_date","invoice_number","phone_number",
            "line_one","line_one_quantity","line_one_unit_price","line_one_total_price",
            "line_two","line_two_quantity","line_two_unit_price","line_two_total_price",
            "line_three","line_three_quantity","line_three_unit_price","line_three_total_price",
            "line_four","line_four_quantity","line_four_unit_price","line_four_total_price",
            "line_five","line_five_quantity","line_five_unit_price","line_five_total_price",
            "total","paid","invoice_type",
        ]
        

class InvoiceSearchForm(forms.ModelForm):
    class Meta:
        model =  Invoice
        fields = ["invoice_number"]
    

class UpdateInvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = [
                "name","invoice_date","invoice_number","phone_number",
                "line_one","line_one_quantity","line_one_unit_price","line_one_total_price",
                "line_two","line_two_quantity","line_two_unit_price","line_two_total_price",
                "line_three","line_three_quantity","line_three_unit_price","line_three_total_price",
                "line_four","line_four_quantity","line_four_unit_price","line_four_total_price",
                "line_five","line_five_quantity","line_five_unit_price","line_five_total_price",
                "total","paid","invoice_type",
            ]
        
    
    
class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = [
            "first_name","last_name","p_number","email","pass1","pass2",
        ]
        

class LoginForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ["pass1","email"]