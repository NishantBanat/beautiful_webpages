from django.shortcuts import render


# Create your views here.
def bill_view(request):
    context = {}
    return render(request, "billing/bill_view.html", context=context)
