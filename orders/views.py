from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from polls.models import Client


def order_create(request):
    cart = Cart(request)
    
    print 'user ****useeeeeeeeer********'
    #print user
    
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            try :
                user = request.user.email
                client = Client.objects.get(email=user)
                order.client = client
                order.save()
            except:
                print 'there is no client'
            for item in cart:
                OrderItem.objects.create(commande=order,
                                        produit=item['product'],
                                        prix=item['price'],
                                        quantite=item['quantity'])  
            # clear the cart
            cart.clear()
            return render(request,
                          'orders/order/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm()
    return render(request,
                  'orders/order/create.html',
                  {'cart': cart, 'form': form})
