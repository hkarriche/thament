from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

# Register your models here.
from .models import  Client, Vendeur, Produit
# from .models import Choice,Client
from .models import Panier, Commande, Facture, Categorie, MessageContact
from .forms import CustomUserChangeForm, CustomUserCreationForm


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

admin.site.register(Client)
admin.site.register(Vendeur)
admin.site.register(Produit)
admin.site.register(Categorie)
admin.site.register(Panier)
admin.site.register(Commande)
admin.site.register(Facture)
admin.site.register(MessageContact)
#admin.site.register(Client, CustomUserAdmin)


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
