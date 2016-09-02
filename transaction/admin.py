from django.contrib import admin

# Register your models here.
from .models import Transaction, TransactionDetails



class DetailInline(admin.TabularInline):
    model = TransactionDetails

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('shopper', 'total_price', 'payment_id', 'is_valid')
    inlines = [DetailInline]

admin.site.register(Transaction, TransactionAdmin)