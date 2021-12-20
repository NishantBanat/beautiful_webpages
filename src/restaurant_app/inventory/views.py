from django.shortcuts import render


# Create your views here.
def inv_land(request):
    context = {}
    return render(request, "inventory/inv_land.html", context=context)


def inv_add(request):
    context = {}
    print("hello inv add !")
    return render(request, "inventory/inv_land.html", context=context)
