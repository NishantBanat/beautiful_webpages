from django.urls import path
from . import views

urlpatterns = [
    path('', views.bill_view, name='bill_view')
]
