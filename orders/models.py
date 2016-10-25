from __future__ import unicode_literals

# Create your models here.
from django.db import models
from polls.models import Produit
from polls.models import Client


#HKA 06.09.2016 add payment method 
class methode_paiement (models.Model):
    nom_methode = models.CharField(max_length=200,null=True)
    def __unicode__(self): 
        return u'%s ' % (self.nom_methode)

class Commande(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE,blank=True,null=True)
    meth_paiemet = models.ForeignKey(methode_paiement, on_delete=models.CASCADE,blank=True,null=True)
    adresse_livraison = models.CharField('Adresse Livraison', max_length=200, default='', blank=True) 
    adresse_facturation = models.CharField('Adresse Facturation', max_length=200, default='', blank=True,null=True) 
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)    
    paid = models.BooleanField(default=False)
    owner = models.CharField('Proprietaire', max_length=70, default='', blank=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Commande {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())
    

class OrderItem(models.Model):
    commande = models.ForeignKey(Commande, related_name='items')
    produit = models.ForeignKey(Produit, 
                                related_name='Commande_items')
    prix = models.DecimalField(max_digits=10, decimal_places=2,blank=True,null=True)
    quantite = models.PositiveIntegerField(default=1)
    

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.prix * self.quantite
    


# class Commande(models.Model):
#     commande_id = models.CharField(max_length=120)
#     owner = models.CharField(max_length=200,null=True) #HKA 06.09.2016 The owner is the id of the client
#     id_clt = models.ForeignKey(Client, on_delete=models.CASCADE)
#     #items = models.ManyToManyField( "CommandeItem", verbose_name = "Factures" )
#     #ref_prod = models.ForeignKey(Produit, on_delete=models.CASCADE)
#     ref_prod = models.ManyToManyField(Produit)
#     #meth_paiemet = models.ForeignKey(methode_paiement, on_delete=models.CASCADE)
#     adresse_livraison = models.CharField('Adresse Livraison', max_length=200, default='', blank=True) 
#     adresse_facturation = models.CharField('Adresse Facturation', max_length=200, default='', blank=True) 
#     date_cmde = models.DateTimeField('Date Commande')
#     # cart = models.ForeignKey(Cart)
#     #status = models.CharField(max_length=120, choices=STATUS_CHOICES, default="Started")
#     # sub_total = models.DecimalField(default=10.99, max_digits=65, decimal_places=2)
#     # tax_total = models.DecimalField(default=0.00, max_digits=65, decimal_places=2)
#     # final_total = models.DecimalField(default=10.99, max_digits=65, decimal_places=2)
#     # timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
#     def reference_produit(self):
#         return self.ref_prod
#     def __unicode__(self):
#         return self.commande_id
