from django import forms
from models import MessageContact, Client, Vendeur, Produit
from registration.forms import RegistrationForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from address.forms import AddressField


class MessageContactForm(forms.ModelForm):
	class Meta :
		model = MessageContact
		fields = ('email','objet','contenu', 'tel')



# class CommandeForm(forms.ModelForm):
#     class Meta:
#         model = Commande
#         fields=('id_clt','adresse_livraison','adresse_facturation')


class MyCustomUserForm(RegistrationForm):
    required_css_class = 'required'

    class Meta:
        model = Vendeur
        fields = ("first_name","last_name","telephone","email")
        fields_required = ['first_name']
        
        


class ClientUserForm(RegistrationForm):
    required_css_class = 'required'

    class Meta:
        model = Client
        fields = ("first_name","last_name","telephone","email")
        fields_required = ['first_name']

        




# class CommandeForm(forms.ModelForm):
#     class Meta:
#         model = Commande
#         fields=('id_clt','adresse_livraison','adresse_facturation')
#     bars = forms.ModelMultipleChoiceField(queryset=Produit.objects.all())

#     def __init__(self, *args, **kwargs):
#         super(CommandeForm, self).__init__(*args, **kwargs)
#         if self.instance:
#             self.fields['bars'].initial = self.instance.bar_set.all()

#     def save(self, *args, **kwargs):
#         # FIXME: 'commit' argument is not handled
#         # TODO: Wrap reassignments into transaction
#         # NOTE: Previously assigned Foos are silently reset
#         instance = super(CommandeForm, self).save(commit=False)
#         self.fields['bars'].initial.update(foo=None)
#         self.cleaned_data['bars'].update(foo=instance)
#         return instance
    













class CustomUserCreationForm(UserCreationForm):
    """
    A form that creates a user, with no privileges, from the given email and
    password.
    """

    def __init__(self, *args, **kargs):
        super(CustomUserCreationForm, self).__init__(*args, **kargs)
        del self.fields['username']

    class Meta:
        model = Vendeur
        fields = ("email",)

class CustomUserChangeForm(UserChangeForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    def __init__(self, *args, **kargs):
        super(CustomUserChangeForm, self).__init__(*args, **kargs)
        del self.fields['username']

    class Meta:
        model = Vendeur
        fields = ("email",)

