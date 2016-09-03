from django.conf.urls import include, url

from registration.backends.hmac.views import RegistrationView

from . import views
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from forms import MyCustomUserForm, ClientUserForm
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
app_name = 'polls'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    # url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^olives/$', views.OliveView.as_view(), name='olives_list'),
    url(r'^oleastre/$', views.OleastreView.as_view(), name='oleastres_list'),
    url(r'^lentisque/$', views.LentisqueView.as_view(), name='lentisques_list'),
    url(r'^miel/$', views.MielView.as_view(), name='miel_list'),
    url(r'^dattes/$', views.DattesView.as_view(), name='dattes_list'),
    url(r'^figues/$', views.FiguesView.as_view(), name='figues_list'),
    url(r'^raisins/$', views.RaisinsView.as_view(), name='raisins_list'),
    url(r'^pistaches/$', views.PistachesView.as_view(), name='pistaches_list'),
    url(r'^contact/$', views.ContactView.as_view(), name='contact_list'),
    url(r'^contact/create$', views.sendMessageContact, name='sendcontact'),

    #HKA 25.08.2016 Vendor views for sign-in & sign up
    url('^register/vendeur', CreateView.as_view(template_name='polls/register_vendeur.html',form_class=MyCustomUserForm,success_url='/polls')),
    url(r'^vendeur/create$', views.registerVendeur, name='createVendeur'),
    url(r'^vendeur/login$',views.LoginVendeurView.as_view(), name='login_vendeur'),
    url(r'^vendeur/authenticate$', views.AuthenticateVendeur, name='createVendeur'),


    #HKA 25.08.2016 Customer views for sign-in & sign up
    url('^register/client', CreateView.as_view(template_name='polls/register_client.html',form_class=ClientUserForm,success_url='/polls')),
    url(r'^client/create$', views.registerClient, name='createClient'),
    url(r'^client/login$',views.LoginVendeurView.as_view(), name='login_vendeur'),
    url(r'^client/authenticate$', views.AuthenticateVendeur, name='createVendeur'),
    url(r'^accounts/register/$',RegistrationView.as_view(form_class=MyCustomUserForm),name='registration_register',),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    #url(r'^site_media/(.*)$', 'django.views.static.serve', {'document_root' : settings.MEDIA_ROOT}),
    url(r'^site_media/(.*)$', serve, {'document_root': settings.MEDIA_ROOT,
    }),

]

