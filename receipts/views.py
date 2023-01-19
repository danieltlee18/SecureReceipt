from django.shortcuts import render
from .models import Receipt, Account, ExpenseCategory


def receipt_list(request):
    receipts = Receipt.objects.all()
    context = {"receipts": receipts}
    return render(request, "receipts/receipt_list.html", context)
