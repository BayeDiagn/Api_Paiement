# payment/forms.py
from django import forms

class PaydunyaForm(forms.Form):
    name = forms.CharField(max_length=100)
    prix_unit = forms.DecimalField(max_digits=10, decimal_places=2)
    quantity = forms.DecimalField(max_digits=10, decimal_places=2)
    