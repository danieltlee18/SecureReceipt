from django.shortcuts import render, redirect
from .models import Receipt
from django.contrib.auth.decorators import login_required
from .forms import ReceiptForm

@login_required
def receipt_list(request):
    receipts = Receipt.objects.filter(purchaser=request.user)
    context = {"receipts": receipts}
    return render(request, "receipts/receipt_list.html", context)

@login_required
def receipt_create(request):
    if request.method == "POST":
        form = ReceiptForm(request.POST)
        if form.is_valid():
            receipt = form.save(False)
            receipt.purchaser = request.user
            receipt.save()
            return redirect("home")
    else:
        form = ReceiptForm()
        context = {"form": form}
        return render(request, "receipts/create_receipt.html", context)
