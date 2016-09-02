import json
from django.http import HttpResponse

from .serializers import ProductSerializer
from .models import Product
from transaction.models import Transaction

from rest_framework.views import APIView
from rest_framework.response import Response


class ProductListView(APIView):

    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
