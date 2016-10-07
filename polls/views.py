from django.shortcuts import get_object_or_404,render

# Create your views here.
from django.http import HttpResponseRedirect,HttpResponse
from django.http import Http404
from django.template import loader
from .models import  Produit, Categorie
from django.views import generic
from django.core.urlresolvers import reverse
from django.utils import timezone
from forms import MessageContactForm
from django.template.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from django. contrib.auth import authenticate, login, logout
from django.contrib import auth
from forms import MyCustomUserForm,ClientUserForm
from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from cart.forms import CartAddProductForm
import operator
from django.db.models import Q
import base64



class IndexView(generic.ListView):
    context_object_name = 'produit_list'
    template_name = 'polls/index.html'

    queryset = Produit.objects.all()


    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['categories'] = Categorie.objects.all()
        cart_product_form = CartAddProductForm()
        context['cart_product_form'] = cart_product_form
        return context


class InactiveView(generic.ListView):
    context_object_name = 'olives_list'
    template_name = 'polls/inactive.html'
    try :
        cat_olives = Categorie.objects.get(nom_categorie="Huile d'olives")
        queryset = Produit.objects.all().filter(cat_prod=cat_olives)
    except :
        queryset = {}

   
     


    def get_context_data(self, **kwargs):
        context = super(InactiveView, self).get_context_data(**kwargs)
        # olives = Produit.objects.all().filter(cat_prod=cat_olives)
        # encoded_string = base64.b64encode(olives.image_prod)
        context['categories'] = Categorie.objects.all()
        cart_product_form = CartAddProductForm()
        context['cart_product_form'] = cart_product_form
        return context


class OliveView(generic.ListView):
    context_object_name = 'olives_list'
    template_name = 'polls/olives.html'
    try :
        cat_olives = Categorie.objects.get(nom_categorie="Huile d'olives")
        queryset = Produit.objects.all().filter(cat_prod=cat_olives)
    except :
        queryset = {}

   
     


    def get_context_data(self, **kwargs):
        context = super(OliveView, self).get_context_data(**kwargs)
        # olives = Produit.objects.all().filter(cat_prod=cat_olives)
        # encoded_string = base64.b64encode(olives.image_prod)
        context['categories'] = Categorie.objects.all()
        cart_product_form = CartAddProductForm()
        context['cart_product_form'] = cart_product_form
        return context

class OleastreView(generic.ListView):
    context_object_name = 'oleastres_list'
    template_name = 'polls/oleastres.html'
    try :
        cat_oleastres = Categorie.objects.get(nom_categorie="Huile d'oleastres")
        queryset = Produit.objects.all().filter(cat_prod=cat_oleastres)
    except :
        queryset = {}

    def get_context_data(self, **kwargs):
        context = super(OleastreView, self).get_context_data(**kwargs)
        context['categories'] = Categorie.objects.all()
        cart_product_form = CartAddProductForm()
        context['cart_product_form'] = cart_product_form
        return context

class LentisqueView(generic.ListView):
    context_object_name = 'lentisques_list'
    template_name = 'polls/lentisques.html'
    try :
        cat_lentisques = Categorie.objects.get(nom_categorie="Huile de lentisques")
        queryset = Produit.objects.all().filter(cat_prod=cat_lentisques)
    except :
        queryset = {}
       

    def get_context_data(self, **kwargs):
        context = super(LentisqueView, self).get_context_data(**kwargs)
        context['categories'] = Categorie.objects.all()
        cart_product_form = CartAddProductForm()
        context['cart_product_form'] = cart_product_form
        return context

class MielView(generic.ListView):
    context_object_name = 'miel_list'
    template_name = 'polls/miel.html'
    #cat_miel = Categorie.objects.get(nom_categorie="Miel")
    try :
        cat_miel = Categorie.objects.get(nom_categorie="Miel")
        queryset = Produit.objects.all().filter(cat_prod=cat_miel)
    except :
        queryset = {}
    

    def get_context_data(self, **kwargs):
        context = super(MielView, self).get_context_data(**kwargs)
        context['categories'] = Categorie.objects.all()
        cart_product_form = CartAddProductForm()
        context['cart_product_form'] = cart_product_form
        return context


class FiguesView(generic.ListView):
    context_object_name = 'figues_list'
    template_name = 'polls/figues.html'
    try :
        cat_figues = Categorie.objects.get(nom_categorie="Figues")
        queryset = Produit.objects.all().filter(cat_prod=cat_figues)
    except :
        queryset = {}
    

    def get_context_data(self, **kwargs):
        context = super(FiguesView, self).get_context_data(**kwargs)
        context['categories'] = Categorie.objects.all()
        cart_product_form = CartAddProductForm()
        context['cart_product_form'] = cart_product_form
        return context

class DattesView(generic.ListView):
    context_object_name = 'dattes_list'
    template_name = 'polls/dattes.html'
    try :
        cat_dattes = Categorie.objects.get(nom_categorie="Dattes")
        queryset = Produit.objects.all().filter(cat_prod=cat_dattes)
    except :
        queryset = {}
    

    def get_context_data(self, **kwargs):
        context = super(DattesView, self).get_context_data(**kwargs)
        context['categories'] = Categorie.objects.all()
        cart_product_form = CartAddProductForm()
        context['cart_product_form'] = cart_product_form
        return context

class RaisinsView(generic.ListView):
    context_object_name = 'raisins_list'
    template_name = 'polls/raisins.html'
    try :
        cat_raisin = Categorie.objects.get(nom_categorie="Raisin sec")
        queryset = Produit.objects.all().filter(cat_prod=cat_raisin)
    except :
        queryset = {}
    

    def get_context_data(self, **kwargs):
        context = super(RaisinsView, self).get_context_data(**kwargs)
        context['categories'] = Categorie.objects.all()
        cart_product_form = CartAddProductForm()
        context['cart_product_form'] = cart_product_form
        return context

class PistachesView(generic.ListView):
    context_object_name = 'pistaches_list'
    template_name = 'polls/pistaches.html'
    try :
        cat_pistaches = Categorie.objects.get(nom_categorie="Pistaches")
        queryset = Produit.objects.all().filter(cat_prod=cat_pistaches)
    except :
        queryset = {}
    

    def get_context_data(self, **kwargs):
        context = super(PistachesView, self).get_context_data(**kwargs)
        context['categories'] = Categorie.objects.all()
        cart_product_form = CartAddProductForm()
        context['cart_product_form'] = cart_product_form
        return context

class ContactView(generic.ListView):
    context_object_name = 'categories' 
    #form = MessageContactForm()
    template_name = 'polls/contact.html'
    queryset = Categorie.objects.all()
    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        form = MessageContactForm()
        context['form'] = form
        return context
# HKA 23.08.2016 define the send message function
def sendMessageContact(request):
    if request.POST:
        form = MessageContactForm(request.POST)
        if form.is_valid():
            form.save()
            #return HttpResponseRedirect(reverse('polls:contact'))
            return HttpResponseRedirect('/polls/contact')
    else :
        form = MessageContactForm()
        args={}
        args.update(csrf(request))
        args['form']=form

        return render_to_response('/polls/contact')
        #*********************#
# HKA 25.08.2016 Function for vendor authentication  and registration
    
def registerVendeur(request):
    if request.method == 'POST':
        form = MyCustomUserForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            # new_user.first_name = username = request.POST.get('first_name','')
            # new_user.last_name = username = request.POST.get('last_name','')
            # new_user.email = username = request.POST.get('Email','')
            new_user.is_staff = True
            new_user.is_active = False
            new_user.save()
            group = Group.objects.get(name='vendeur')
            group.user_set.add(new_user)
            #new_user.groups = group
            # new_user.save()
            
            return HttpResponseRedirect("/polls")
    else:
        form = MyCustomUserForm()
    return render(request, "polls/register_vendeur.html", {
        'form': form,
    })

class LoginClientView(generic.ListView):
    context_object_name = 'produits_list'
    template_name = 'polls/login_client.html'
    queryset = Produit.objects.all()
    

    def get_context_data(self, **kwargs):
        context = super(LoginClientView, self).get_context_data(**kwargs)
        context['categories'] = Categorie.objects.all()
        cart_product_form = CartAddProductForm()
        context['cart_product_form'] = cart_product_form
        return context

class LoginVendeurView(generic.ListView):
    context_object_name = 'produits_list'
    template_name = 'polls/login_vendeur.html'
    queryset = Produit.objects.all()
    

    def get_context_data(self, **kwargs):
        context = super(LoginVendeurView, self).get_context_data(**kwargs)
        context['categories'] = Categorie.objects.all()
        cart_product_form = CartAddProductForm()
        context['cart_product_form'] = cart_product_form
        return context

def AuthenticateVendeur(request):
    username = request.POST.get('Username','')
    password = request.POST.get('Password','')
    user = authenticate(username=username,password=password)
    if user is not None :
        if user.is_active:
            auth.login(request,user)
            return HttpResponseRedirect('/admin')
        else :
            return HttpResponseRedirect('/polls/inactive')   

 
      #*********************#
# HKA 25.08.2016 Function for customer authentication 
def registerClient(request):
    if request.method == 'POST':
        form = ClientUserForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            # new_user.first_name = username = request.POST.get('first_name','')
            # new_user.last_name = username = request.POST.get('last_name','')
            # new_user.email = username = request.POST.get('Email','')
            new_user.is_staff = True
            new_user.save()
            
            group = Group.objects.get(name='client')
            group.user_set.add(new_user)
            

            return HttpResponseRedirect("/polls")
    else:
        form = ClientUserForm()
    return render(request, "polls/register_client.html", {
        'form': form,
    })


#HKA 30.09.2016 create an account after sign-in or sign-up

class OrderSigninView(generic.ListView):
    context_object_name = 'produits_list'
    template_name = 'polls/order_client.html'
    queryset = Produit.objects.all()
    

    def get_context_data(self, **kwargs):
        context = super(OrderSigninView, self).get_context_data(**kwargs)
        context['categories'] = Categorie.objects.all()
        cart_product_form = CartAddProductForm()
        context['cart_product_form'] = cart_product_form
        return context
#HKA 30.09.2016 Redirect the client to create order
def AuthenticateOrderClient(request):
    username = request.POST.get('Username','')
    password = request.POST.get('Password','')
    user = authenticate(username=username,password=password)
    if user is not None :
        if user.is_active:
            auth.login(request,user)
            return HttpResponseRedirect('/orders/create/')
        else :
            return HttpResponseRedirect('/polls/inactive') 

def registerOrderClient(request):
    
    if request.method == 'POST':
        form = ClientUserForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            # new_user.first_name = username = request.POST.get('first_name','')
            # new_user.last_name = username = request.POST.get('last_name','')
            # new_user.email = username = request.POST.get('Email','')
            new_user.is_staff = True
            new_user.save()
            
            group = Group.objects.get(name='client')
            group.user_set.add(new_user)
           

            return HttpResponseRedirect("/polls/order/signin")
    else:
        form = ClientUserForm()
    return render(request, "polls/register_order_client.html", {
        'form': form,
    })

class BlogSearchListView(IndexView):
    """
    Display a Blog List page filtered by the search query.
    """
    paginate_by = 10

    def get_queryset(self):
        result = super(BlogSearchListView, self).get_queryset()

        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            result = result.filter(
                reduce(operator.and_,
                       (Q(title__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(content__icontains=q) for q in query_list))
            )

        return result

# def search(request):
#     print (i am here')
#     new_results = []
#     error = True
#     if "q" in request.GET: 
#         query = request.GET["q"].strip()
#         results = graph_search.main(query)
#         for result in results:
#             result[3] = result[3].decode('unicode_escape').encode('ascii', 'ignore')
#             new_results.append(result)
#         new_results = list(reversed(sorted(new_results, key=itemgetter(4))))
#         return render(request, 'search.html',
#                       {'results': new_results, 'query': query})
#     return render(request, "polls/search.html", {'error': error})

def search(request):
    print (' i am in search')
    try:
        q = request.GET.get('q')
    except:
        q = None
    
    if q:
        products = Produit.objects.filter(ref_prod__icontains=q)
        context = {'query': q, 'products': products}
        template = 'polls/results.html'  
    else:
        template = 'polls/index.html' 
        context = {}
    return render(request, template, context)