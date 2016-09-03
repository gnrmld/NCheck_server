from django.conf.urls import url

from . import views
from .views import TransactionView, TransactionReturnView, TransactionConfirmationView

urlpatterns = [
    url(r'create/?', TransactionView.as_view(), name='create'),
    url(r'detail/(?P<payment_id>\w.+)/$', TransactionReturnView.as_view(), name='transaction_return'),
    url(r'confirmation/(?P<message>\w+)/$', TransactionConfirmationView.as_view(), name='confirmation')
]