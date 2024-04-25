# paytech_project/urls.py
from django.urls import path
from .views import payment_canceled, payment_done, payment_view




urlpatterns = [
    path('', payment_view, name='paytech_payment'),
    path('payment-done/',payment_done, name='payment_done'),
    path('payment-canceled/',payment_canceled, name='payment_canceled'),
]