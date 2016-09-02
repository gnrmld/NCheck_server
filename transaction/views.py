import ast

from django.conf import settings

from product.models import Product
from .models import Transaction

from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class TransactionView(APIView):
    """Process Transaction Detail"""

    def post(self, request, format=None):
        items = ast.literal_eval(request.POST.get("items"))
        payment_id = request.POST.get('payment_id')
        total_price = request.POST.get('total_price')
        transaction = Transaction()
        transaction.shopper_id = 1
        transaction.total_price = total_price
        transaction.payment_id = payment_id
        if not Transaction.objects.filter(payment_id=payment_id):
            transaction.save()
            for item in items:
                product = Product.objects.get(barcode=item.get('barcode'))
                product.quantity -= item.get('quantity')
                product.save()
                transaction.product.add(product)

        context = {
            "url": settings.HOST_URL + 'transaction/' + transaction.payment_id
        }
        return Response(context)


class TransactionReturnView(APIView):
    """Return transaction view to client"""

    def get(self, request, *args, **kwargs):
        print (self.kwargs.get('payment_id'))
        if Transaction.objects.filter(payment_id=self.kwargs.get('payment_id')):
            message = 'SUCCESS!'
        else:
            message = 'FAIL'

        context = {
            "success_message": message,
        }

        return Response(context)