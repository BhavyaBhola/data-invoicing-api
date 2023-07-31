from django.db import models
from datetime import date
# Create your models here.


class Invoice(models.Model):
    
    date = models.DateField(null=True , default=date.today().strftime('%Y-%m-%d'))
    invoice_no = models.IntegerField()
    customer_name = models.CharField(max_length=120)

    def __str__(self):
        return self.customer_name

class InvoiceDetail(models.Model):
    invoice = models.ForeignKey(Invoice , on_delete=models.CASCADE , related_name='invoice')
    description = models.CharField(max_length=200)
    quantity = models.IntegerField()
    unit_price = models.IntegerField()
    price = models.IntegerField()
