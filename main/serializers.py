from rest_framework import serializers
from .models import Invoice , InvoiceDetail



    

class InvoiceDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = InvoiceDetail
        fields = ['description' , 'quantity' , 'unit_price', 'price']


class InvoiceSerializer(serializers.ModelSerializer):
    invoice = InvoiceDetailSerializer(many=True)
    class Meta:
        model = Invoice
        fields = ['customer_name' , 'invoice_no' , 'date' , 'invoice'] 

    def create(self,validated_data):
        
        invoice_data = validated_data.pop('invoice')
        print(invoice_data)
        inv = Invoice.objects.create(**validated_data)
        for invoices in invoice_data:
            InvoiceDetail.objects.create(invoice=inv , **invoices)
        return inv