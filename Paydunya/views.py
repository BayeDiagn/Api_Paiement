from decimal import Decimal
from django.shortcuts import render, redirect
from .forms import PaydunyaForm
import paydunya
from paydunya import InvoiceItem, Store,Invoice
from Api_Payment.settings import PAYDUNYA_ACCESS_TOKENS



# Activer le mode 'test'. Le debug est à False par défaut
paydunya.debug = True

# Configurer les clés d'API
paydunya.api_keys = PAYDUNYA_ACCESS_TOKENS

# Configuration des informations de votre service/entreprise
store = Store(name='Paiement with Paydunya')




def payment_view(request):
    if request.method == 'POST':
        form = PaydunyaForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['nom']
            unit_price = form.cleaned_data['prix_unite']
            quantity = form.cleaned_data['quantite']

            total_price = int(quantity)*int(unit_price)

            #Ajout d'un produit dans la facture
            items = [
                InvoiceItem(
                    name=name,
                    quantity=int(quantity),
                    unit_price=str(unit_price),
                    total_price=str(total_price),
                    description=name
                ),
            ]
    
            invoice = paydunya.Invoice(store)
            
            
        
            invoice.return_url = "https://localhost:8000/payment-done/"
            invoice.cancel_url = "https://localhost:8000/payment-canceled/"
        
            invoice.add_items(items)
        
        
            successful, response = invoice.create()
            #print(response)
            if successful:
                return redirect(response.get('response_text'))
            # else:
            #     print(response)

    else:
        form = PaydunyaForm()

    return render(request, 'Paydunya/paydunya_form.html', {'form': form})




#Redirection apres paiement 
def payment_done(request):
    
    token = request.GET.get('token')
    invoice = Invoice(store)
    successful, response = invoice.confirm(token)
    
    if successful:
        #Vous pouvez interagir avec la base de donnee ou faire d'autres actions une fois que le client a bien payer
        pass
    
    return redirect('paydunya_payment')
    
      
  
#Annulation du paiement   
def payment_canceled(request):
    
    return redirect('paydunya_payment')



#Accueil
def home_page(request):
    
    return render(request, 'index.html')
