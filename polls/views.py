from django.shortcuts import get_object_or_404,render

# Create your views here.
from django.http import HttpResponseRedirect,HttpResponse
from django.http import Http404
from django.template import loader
from .models import Question,Choice, Produit, Categorie
from django.views import generic
from django.core.urlresolvers import reverse
from django.utils import timezone
from forms import MessageContactForm
from django.template.context_processors import csrf

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'categories'

    def get_queryset(self):
              
        return Categorie.objects.all( )

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
    
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


class OliveView(generic.ListView):
    context_object_name = 'olives_list'
    template_name = 'polls/olives.html'
    queryset = Produit.objects.all()


    def get_context_data(self, **kwargs):
        context = super(OliveView, self).get_context_data(**kwargs)
        context['categories'] = Categorie.objects.all()
        return context

class OleastreView(generic.ListView):
    context_object_name = 'oleastres_list'
    template_name = 'polls/oleastres.html'
    queryset = Produit.objects.all()
    

    def get_context_data(self, **kwargs):
        context = super(OleastreView, self).get_context_data(**kwargs)
        context['categories'] = Categorie.objects.all()
        return context

class LentisqueView(generic.ListView):
    context_object_name = 'lentisques_list'
    template_name = 'polls/lentisques.html'
    queryset = Produit.objects.all()
    

    def get_context_data(self, **kwargs):
        context = super(LentisqueView, self).get_context_data(**kwargs)
        context['categories'] = Categorie.objects.all()
        return context

class MielView(generic.ListView):
    context_object_name = 'miel_list'
    template_name = 'polls/miel.html'
    queryset = Produit.objects.all()
    

    def get_context_data(self, **kwargs):
        context = super(MielView, self).get_context_data(**kwargs)
        context['categories'] = Categorie.objects.all()
        return context

class LentisqueView(generic.ListView):
    context_object_name = 'dattes_list'
    template_name = 'polls/dattes.html'
    queryset = Produit.objects.all()
    

    def get_context_data(self, **kwargs):
        context = super(LentisqueView, self).get_context_data(**kwargs)
        context['categories'] = Categorie.objects.all()
        return context

class FiguesView(generic.ListView):
    context_object_name = 'figues_list'
    template_name = 'polls/figues.html'
    queryset = Produit.objects.all()
    

    def get_context_data(self, **kwargs):
        context = super(FiguesView, self).get_context_data(**kwargs)
        context['categories'] = Categorie.objects.all()
        return context

class DattesView(generic.ListView):
    context_object_name = 'dattes_list'
    template_name = 'polls/dattes.html'
    queryset = Produit.objects.all()
    

    def get_context_data(self, **kwargs):
        context = super(DattesView, self).get_context_data(**kwargs)
        context['categories'] = Categorie.objects.all()
        return context

class RaisinsView(generic.ListView):
    context_object_name = 'raisins_list'
    template_name = 'polls/raisins.html'
    queryset = Produit.objects.all()
    

    def get_context_data(self, **kwargs):
        context = super(RaisinsView, self).get_context_data(**kwargs)
        context['categories'] = Categorie.objects.all()
        return context

class PistachesView(generic.ListView):
    context_object_name = 'pistaches_list'
    template_name = 'polls/pistaches.html'
    queryset = Produit.objects.all()
    

    def get_context_data(self, **kwargs):
        context = super(PistachesView, self).get_context_data(**kwargs)
        context['categories'] = Categorie.objects.all()
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
    



