from django import forms
from models import MessageContact, Client, Vendeur
from registration.forms import RegistrationForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class MessageContactForm(forms.ModelForm):
	class Meta :
		model = MessageContact
		fields = ('email','objet','contenu', 'tel')


class MyCustomUserForm(RegistrationForm):
    class Meta:
        model = Vendeur
        fields = ("first_name","last_name","email","username")

class ClientUserForm(RegistrationForm):
    class Meta:
        model = Client
        fields = ("first_name","last_name","email","username")














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
