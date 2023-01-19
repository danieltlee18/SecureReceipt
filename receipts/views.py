from django.shortcuts import render
from .models import Receipt, Account, ExpenseCategory
from django.contrib.auth.decorators import login_required


@login_required
def receipt_list(request):
    receipts = Receipt.objects.filter(purchaser=request.user)
    context = {"receipts": receipts}
    return render(request, "receipts/receipt_list.html", context)
