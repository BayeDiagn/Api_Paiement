# payment/forms.py
from django import forms

class PaytechForm(forms.Form):
    item_name = forms.CharField(max_length=100)
    item_price = forms.DecimalField(max_digits=10, decimal_places=2)
    