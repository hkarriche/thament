from django.contrib import admin
from .models import Commande, OrderItem,methode_paiement
from polls.models import Client, Produit, Vendeur

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['produit']
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','client','paid','meth_paiemet','adresse_livraison', 
                    'adresse_facturation','created', 'updated','owner']
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
        	produit = Produit.objects.all().filter(owner=kheddame)
        	print ('here product *********')
        	print produit
        	listorder = {}
        	listorder = OrderItem.objects.all().filter(produit=produit)
        	print ('here orderitem *********')
        	print listorder
        	return Commande.objects.all().filter(id=61)

        # else :
        # 	try :
        # 		client = Client.objects.get(email=kheddame)
        # 		if client is not None :
        # 			return Commande.objects.all().filter(owner=kheddame)
        # 	except :
        # 		print ('there is no client')

        # 	try :
        # 		vendeur = Vendeur.objects.get(email=kheddam)
        # 		if vendeur is not None :
        # 			
        # 			orderitems = Produit.objects.all().filter(owner=vendeur)
        # 			return Commande.objects.all().filter(id=61)
        # 	except :
        # 		print ('there is no vendor')
        	
        
        

admin.site.register(Commande, OrderAdmin)
admin.site.register(methode_paiement)