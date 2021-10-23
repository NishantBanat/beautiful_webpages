from django.urls import path
from . import views

urlpatterns = [
    path('/', views.inv_land, name='inv_land')
]