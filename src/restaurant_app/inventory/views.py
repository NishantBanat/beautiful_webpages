from django.shortcuts import render


# Create your views here.
def inv_land(request):
    context = {}
    return render(request, "inventory/inv_land.html", context=context)
