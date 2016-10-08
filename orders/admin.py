from django.contrib import admin
from .models import Commande, OrderItem,methode_paiement
from polls.models import Client, Produit, Vendeur
from django.db import connection
from django.core.urlresolvers import reverse







class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['produit']
    extra = 1


def order_detail(obj):
    return '<a href="{}">View</a>'.format(
        reverse('orders:admin_order_detail', args=[obj.id]))
order_detail.allow_tags = True 


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','client','paid','meth_paiemet','adresse_livraison', 
                    'adresse_facturation','created', 'updated','owner',order_detail]
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]

    def get_queryset(self, request):
        kheddame = str(request.user.email)
        try :
        		client = Client.objects.get(email=kheddame)
        		if client is not None :
        			return Commande.objects.all().filter(owner=kheddame)
        except :
        	
        	client = None        
        if request.user.is_superuser:
        	return Commande.objects.all()
        if client is not None :
        	return Commande.objects.all().filter(owner=kheddame)
        else :
            ss = Produit.objects.all().filter(owner=kheddame)
            dd = OrderItem.objects.filter(produit__in=ss)
            return Commande.objects.filter(id__in=[p.commande_id for p in dd])
        	
     
        

admin.site.register(Commande, OrderAdmin)
admin.site.register(methode_paiement)