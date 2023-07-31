from django.shortcuts import render
from .serializers import InvoiceDetailSerializer , InvoiceSerializer
from .models import Invoice , InvoiceDetail
from rest_framework.views import APIView
from rest_framework.response import Response 

# Create your views here.

class invoiceView(APIView):
    def get(self , request):
        obj = Invoice.objects.all()
        serializers = InvoiceSerializer(obj , many=True)

        return Response(serializers.data)
    
    def post(self , request):
        data = request.data
        serializers = InvoiceSerializer(data=data)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        
        return Response(serializers.errors)