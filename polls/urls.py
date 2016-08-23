from django.conf.urls import url

from . import views


app_name = 'polls'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^olives/$', views.OliveView.as_view(), name='olives_list'),
    url(r'^oleastre/$', views.OleastreView.as_view(), name='oleastres_list'),
    url(r'^lentisque/$', views.LentisqueView.as_view(), name='lentisques_list'),
    url(r'^miel/$', views.MielView.as_view(), name='miel_list'),
    url(r'^dattes/$', views.DattesView.as_view(), name='dattes_list'),
    url(r'^figues/$', views.FiguesView.as_view(), name='figues_list'),
    url(r'^raisins/$', views.RaisinsView.as_view(), name='raisins_list'),
    url(r'^pistaches/$', views.PistachesView.as_view(), name='pistaches_list'),
    url(r'^contact/$', views.ContactView.as_view(), name='contact_list'),
]