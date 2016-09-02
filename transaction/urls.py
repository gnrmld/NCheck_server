from django.conf.urls import url

from . import views
from .views import TransactionView, TransactionReturnView

urlpatterns = [
    url(r'create/?', TransactionView.as_view(), name='create'),
    url(r'(?P<payment_id>\w+)/$', TransactionReturnView.as_view(), name='transaction_return'),

]