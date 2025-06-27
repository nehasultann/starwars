from django.urls import path
from .views import luke_and_father

urlpatterns = [
    path('', luke_and_father),
]
