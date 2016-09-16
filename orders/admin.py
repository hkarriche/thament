from django.contrib import admin
from .models import Commande, OrderItem,methode_paiement

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['produit']
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','client','paid','meth_paiemet','adresse_livraison', 
                    'adresse_facturation','created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]
    
admin.site.register(Commande, OrderAdmin)
admin.site.register(methode_paiement)