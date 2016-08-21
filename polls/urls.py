from django.conf.urls import url

from . import views


app_name = 'polls'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^olives/$', views.OliveView.as_view(), name='olives'),
    url(r'^oleastre/$', views.IndexView.as_view(), name='oleastre'),
    url(r'^lentisque/$', views.IndexView.as_view(), name='lentisque'),
    url(r'^miel/$', views.IndexView.as_view(), name='miel'),
    url(r'^dattes/$', views.IndexView.as_view(), name='dattes'),
]