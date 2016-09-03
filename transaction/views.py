import ast

from django.conf import settings
from django.http import Http404
from django.db.models import Sum

from product.models import Product, Category
from .models import Transaction, TransactionDetails

from rest_framework.views import APIView
from rest_framework.response import Response


class TransactionView(APIView):
    """Process Transaction Detail"""

    def post(self, request, *args, **kwargs):
        items = request.data.get("items")
        payment_id = request.data.get('payment_id')
        total_price = request.data.get('total_price')
        transaction = Transaction()
        transaction.shopper_id = 1
        transaction.total_price = float(total_price)
        transaction.payment_id = payment_id




        if not Transaction.objects.filter(payment_id=payment_id):
            transaction.save()
            for item in items:
                product = Product.objects.get(barcode=item.get('barcode'))
                product.quantity -= int(item.get('quantity'))
                product.save()

                transaction_detail = TransactionDetails()
                transaction_detail.product_id = product.id
                transaction_detail.transaction_id = transaction.id
                transaction_detail.quantity = int(item.get('quantity'))
                transaction_detail.save()

                category = Category.objects.get(id=product.category.id)
                category.total_sale += int(item.get('quantity'))
                category.save()

                # total_quantity = TransactionDetails.objects.filter(product__category=product.category).aggregate(Sum('quantity'))
                # sold_quantity = TransactionDetails.objects.filter(product=product).aggregate(Sum('quantity'))
                # rating = (sold_quantity['quantity__sum'] / total_quantity['quantity__sum']) * 100

                # product.rating = rating


        context = {
            "url": settings.HOST_URL + 'transaction/' + transaction.payment_id,
            "message": 'Thanks for shopping with us!',
        }
        return Response(context)


class TransactionReturnView(APIView):
    """Return transaction view to client"""

    def get(self, request, *args, **kwargs):
        try:
            transaction = Transaction.objects.get(payment_id=self.kwargs.get('payment_id'))
            if transaction.is_valid:
                transaction.is_valid = False
                transaction.save()
                message = 'Validated successfully!'
                status = True
            else:
                message = 'Code not valid anymore'
                status = False
        except Transaction.DoesNotExist as e:
            print(e)
            raise Http404()

        context = {
            "message": message,
            "status": status
        }

        return Response(context)