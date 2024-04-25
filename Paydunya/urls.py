# paytech_project/urls.py
from django.urls import path
from .views import home_page, payment_canceled, payment_done, payment_view




urlpatterns = [
    path('',home_page, name='home'),
    path('paydunya/', payment_view, name='paydunya_payment'),
    path('payment-done/',payment_done, name='payment_done'),
    path('payment-canceled/',payment_canceled, name='payment_canceled'),
    
]