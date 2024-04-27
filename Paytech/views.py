from django.shortcuts import render, redirect
from .forms import PaytechForm
from .utils import PayTech
from Api_Payment.settings import paytech_api_key,paytech_api_secret
import uuid








def payment_view(request):
    if request.method == 'POST':
        form = PaytechForm(request.POST)
        if form.is_valid():
            item_name = form.cleaned_data['item_name']
            item_price = form.cleaned_data['item_price']
            

            
            # Instanciation de la classe PayTech
            pay_tech = PayTech(paytech_api_key, paytech_api_secret)
        
            # Configuration des paramètres de la requête de paiement
            pay_tech.setQuery({
                'item_name': item_name,
                'item_price': item_price,
                'command_name': f"Paiement {item_name} via PayTech"
            })
            pay_tech.setTestMode(True)
            pay_tech.setCurrency('XOF')
            pay_tech.setRefCommand(str(uuid.uuid4()))
            pay_tech.setNotificationUrl({
                'ipn_url': 'https://192.168.1.10:8000/ipn',
                'success_url': 'https://192.168.1.56:8000/paytech/payment-done/',
                'cancel_url': 'https://192.168.1.56:8000/paytech/payment-canceled/',
            })
            pay_tech.setMobile(False)
        
            # Envoi de la requête de paiement
            response = pay_tech.send()

            if response['success'] == 1:
                redirect_url = response['redirect_url']
                return redirect(redirect_url)
            else:
                
                error_message = ', '.join(response['errors'])
                form.add_error('item_price', error_message)
                #print(error_message)
    else:
        form = PaytechForm()

    return render(request, 'Paytech/paytech_form.html', {'form': form})




#Redirection apres paiement 
def payment_done(request):
    #Vous pouvez interagir avec la base de donnee ou faire d'autres actions une fois que le client a bien payer
    
    return redirect('paytech_payment')
    
      
  
#Annulation du paiement   
def payment_canceled(request):
    
    return redirect('paytech_payment')