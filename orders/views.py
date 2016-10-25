from django.shortcuts import render
from .models import OrderItem, Commande
from .forms import OrderCreateForm
from cart.cart import Cart
from polls.models import Client
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.conf import settings 
from django.http import HttpResponse
from django.template.loader import render_to_string
import weasyprint

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
                user = request.user.email
                client = Client.objects.get(email=user)
                order.owner = str(client)
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

#HKA 08.10.2016 The staff_member_required decorator checks that both is_active and is_staff fields of the user requesting the page are set to True

@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Commande, id=order_id)
    return render(request,
                  'orders/order/detail.html',
                  {'order': order})   


@staff_member_required
def admin_order_pdf(request, order_id):
    order = get_object_or_404(Commande, id=order_id)
    html = render_to_string('orders/order/pdf.html',
                            {'order': order})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename=\
        "order_{}.pdf"'.format(order.id)
    weasyprint.HTML(string=html).write_pdf(response,
        )
    return response