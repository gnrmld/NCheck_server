from django.conf.urls import url

from . import views
from .views import ProductListView

urlpatterns = [
    url(r'list/', ProductListView.as_view(), name='list'),

]