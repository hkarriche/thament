from django import forms
from models import MessageContact

class MessageContactForm(forms.ModelForm):
	class Meta :
		model = MessageContact
		fields = ('email','objet','contenu', 'tel')
