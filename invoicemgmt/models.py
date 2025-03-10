from django.db import models

class Invoice(models.Model):
    comments = models.TextField(max_length=3000, default='', blank=True, null=True)
    invoice_number = models.IntegerField(blank=True, null=True)
    invoice_date = models.DateField(blank=True, null=True)
    name = models.CharField('customer Name', max_length=120, default='', blank=True, null=True)
    
    line_one = models.CharField('Line One', max_length=120, blank=True, null=True)
    line_one_quantity = models.IntegerField('Quantity', default=0, blank=True, null=True)
    line_one_unit_price = models.IntegerField("unit Price(D)", default=0, blank=True, null=True)
    line_one_total_price = models.IntegerField('Line Total(D)', default=0, blank=True, null=True)
    
    line_two = models.CharField('Line Two', max_length=120, blank=True, null=True)
    line_two_quantity = models.IntegerField('Quantity', default=0, blank=True, null=True)
    line_two_unit_price = models.IntegerField("unit Price(D)", default=0, blank=True, null=True)
    line_two_total_price = models.IntegerField('Line Total(D)', default=0, blank=True, null=True)
    
    line_three = models.CharField('Line Three', max_length=120, blank=True, null=True)
    line_three_quantity = models.IntegerField('Quantity', default=0, blank=True, null=True)
    line_three_unit_price = models.IntegerField("unit Price(D)", default=0, blank=True, null=True)
    line_three_total_price = models.IntegerField('Line Total(D)', default=0, blank=True, null=True)
    
    line_four = models.CharField('Line Four', max_length=120, blank=True, null=True)
    line_four_quantity = models.IntegerField('Quantity', default=0, blank=True, null=True)
    line_four_unit_price = models.IntegerField("unit Price(D)", default=0, blank=True, null=True)
    line_four_total_price = models.IntegerField('Line Total(D)', default=0, blank=True, null=True)
    
    line_five = models.CharField('Line Five', max_length=120, blank=True, null=True)
    line_five_quantity = models.IntegerField('Quantity', default=0, blank=True, null=True)
    line_five_unit_price = models.IntegerField("unit Price(D)", default=0, blank=True, null=True)
    line_five_total_price = models.IntegerField('Line Total(D)', default=0, blank=True, null=True)
    
    phone_number = models.CharField(max_length=120, default='', blank=True, null=True)
    total = models.IntegerField(default='0', blank=True, null=True)
    balance = models.IntegerField(default='0', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    
    last_updated = models.DateTimeField(auto_now=True, blank=True)
    paid = models.BooleanField(default=False)
    invoice_type_choice = (
        ('Receipt', 'Receipt'),
        ('Proforma Invoice', 'Proforma Invoice'),
        ('Invoice', 'Invoice'),
    )
    
    invoice_type = models.CharField(max_length=50, default='', blank=True, null=True, choices=invoice_type_choice)
    
    def __str__(self):
        return f"{self.name} : {self.invoice_number}"
    

class Registration(models.Model):
    first_name = models.CharField(max_length=120,blank=True,null=True)
    last_name = models.CharField(max_length=120,blank=True,null=True)
    p_number = models.CharField(max_length=120,default='',blank=True,null=True)
    email = models.EmailField(max_length=120,blank=True,null=True)
    pass1 = models.CharField(max_length=15,blank=True,null=True)
    pass2 = models.CharField(max_length=15,blank=True,null=True)
    
    
    def __str__(self):
        return f"{self.first_name} : {self.last_name}"