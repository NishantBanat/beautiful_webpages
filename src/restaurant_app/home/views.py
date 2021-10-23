from django.shortcuts import render


# Create your views here.
def index(request):
    context = {}
    return render(request, template_name="home/home_page.html", context=context)
