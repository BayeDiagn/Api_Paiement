# payment/forms.py
from django import forms

class PaydunyaForm(forms.Form):
    nom = forms.CharField(max_length=100)
    prix_unite = forms.DecimalField(max_digits=10, decimal_places=2)
    quantite = forms.DecimalField(max_digits=10, decimal_places=2)
    