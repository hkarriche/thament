from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

# Register your models here.
from .models import  Client, Vendeur, Produit
# from .models import Choice,Client
from .models import Panier, Facture, Categorie, MessageContact
from .forms import CustomUserChangeForm, CustomUserCreationForm
from orders.models import OrderItem, Commande


class ProduitInline(admin.TabularInline):
    model = Produit
    fields = ('ref_prod','des_prod','prix_prod','cat_prod')


class CategorieAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields': ['nom_categorie']}),
        (None, {'fields': ['url_categorie']}),
    ]
    #inlines = [CategorieInline]
    list_display = ('nom_categorie','url_categorie')
    list_filter = ['nom_categorie']
    search_fields = ['nom_categorie']
    


class MessageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields': ['objet']}),
        (None, {'fields': ['contenu']}),
        (None, {'fields': ['email']}),
        (None, {'fields': ['tel']}),
    ]
    list_display = ('objet','contenu','email','tel')



class ProduitAdmin(admin.ModelAdmin):
    def level(self, obj):
        return obj.cat_prod.nom_categorie
    fieldsets = [
        (None,{'fields': ['ref_prod']}),
        (None, {'fields': ['des_prod']}),
        (None, {'fields': ['prix_prod']}),
        (None, {'fields': ['remise_prod']}),
        (None, {'fields': ['cat_prod']}),
        (None, {'fields': ['image_prod']}),
        (None, {'fields': ['bulletin_analyse']}),
        (None, {'fields': ['owner']}),
        #(None, {'fields': ['level']}),


    ]
    
    list_display = ('ref_prod','des_prod','prix_prod','cat_prod','remise_prod','categorie_produit','bulletin_analyse','image_prod','owner')
    # def categorie_produitt(self):
    #     return self.cat_prod.nom_categorie
    #qs = super(PageAdmin, self).queryset(request)
    #print qs

    # def save_model(self, request, obj, form, change):
    #     if not change:
    #         obj.owner = request.user
    #         obj.save()
    def get_changeform_initial_data(self, request):
        get_data = super(ProduitAdmin, self).get_changeform_initial_data(request)
        get_data['owner'] = request.user
        return get_data
    def get_queryset(self, request):
        
        if request.user.is_superuser:
            return Produit.objects.all()
        else :
            return Produit.objects.all().filter(owner = request.user)

class PanierAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields': ['id_clt']}),
        (None, {'fields': ['ref_prod']}),
        (None, {'fields': ['quantite_produit']}),
        

    ]
    list_display = ('id_clt','quantite_produit','reference_produit')

 

class FactureAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields': ['id_clt']}),
        #(None, {'fields': ['id_cmde']}),
        (None, {'fields': ['montant_fact']}),
       
        

    ]
    list_display = ('id_clt','montant_fact')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.owner = request.user
            obj.save()
    def get_queryset(self, request):
        
        if request.user.is_superuser:
            return Facture.objects.all()
        else :
            kheddame = str(request.user.email)
            return Facture.objects.all().filter(owner=kheddame)


# class CommandeAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,{'fields': ['id_clt']}),
#         #(None, {'fields': ['ref_prod']}),
#         (None, {'fields': ['date_cmde']}),
#         #(None, {'fields': ['meth_paiemet']}),
#         (None, {'fields': ['adresse_livraison']}),
#         (None, {'fields': ['adresse_facturation']}),
#         (None, {'fields': ['ref_prod']}),
#         # (None, {'fields': ['sub_total']}), 
#         # (None, {'fields': ['tax_total']}),
#         # (None, {'fields': ['final_total']}),

#     ]
#     list_display = ('id_clt','reference_produit','date_cmde','adresse_livraison','adresse_facturation')
#     #inlines = (ProduitInline,)

# HKA 01.09.2016 Display categorie in produit list display

def unbound_callable(produit):
    return produit.cat_prod.nom_categorie
class ProduitInline(admin.TabularInline):
    model = Produit
    fields = ('ref_prod', 'model_callable')
 


 #HKA 04.05.2016 Display clients for vendors, the client must have an order for this vendor   


class ClientInline(admin.TabularInline):
    model = Client
    extra = 1

class ClientAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','telephone']
    inlines = [ClientInline]

    def get_queryset(self, request):
        kheddame = str(request.user.email)       
        if request.user.is_superuser:
            return Client.objects.all()
        else :
            ss = Produit.objects.all().filter(owner=kheddame)
            dd = OrderItem.objects.filter(produit__in=ss)
            zz = Commande.objects.filter(id__in=[p.commande_id for p in dd])
            return Client.objects.filter(email__in=[p.owner for p in zz])


admin.site.register(Client,ClientAdmin)
admin.site.register(Vendeur)
admin.site.register(Produit,ProduitAdmin)
admin.site.register(Categorie,CategorieAdmin)
admin.site.register(Panier,PanierAdmin)
#admin.site.register(Commande,CommandeAdmin)
admin.site.register(Facture,FactureAdmin)
admin.site.register(MessageContact,MessageAdmin)


# admin.site.register(CartItem)
# admin.site.register(Item) 
# admin.site.register(Screenshots)
# admin.site.register(ContactRequest)

# class ChoiceInline(admin.TabularInline):
#     model = Choice
#     extra = 5

# # HKA 10.08.2016 inhance the display of the model Question
# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         ('None',               {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date']}),
#     ]
#     inlines = [ChoiceInline]
#     list_display = ('question_text', 'pub_date', 'was_published_recently')
#     list_filter = ['pub_date']
#     search_fields = ['question_text']

# admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)
# class useriline(admin.TabularInline):
#     model = UserDetails
#     extra = 3
# class UserAdmin(admin.ModelAdmin):
#     inlines = [useriline]
# admin.site.register(UserDetails, UserAdmin)
# admin.site.register(Client)


class CustomUserAdmin(UserAdmin):
    # The forms to add and change user instances

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference the removed 'username' field
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)