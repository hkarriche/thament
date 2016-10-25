from __future__ import unicode_literals
import datetime
from django.core import validators
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType


class CustomUserManager(BaseUserManager):
    def create_user(self, email=None, password=None, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')
        email = CustomUserManager.normalize_email(email)
        user = self.model(email=email,
                          is_staff=False, is_active=True, is_superuser=False,
                          last_login=now, date_joined=now, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        u = self.create_user(email, password, **extra_fields)
        u.is_staff = True
        u.is_active = True
        u.is_superuser = True
        u.save(using=self._db)
        return u
class Person(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email (Utilisateur)'), unique=True)
    #username = models.CharField('Utilisateur', unique=True, max_length=70, default='', blank=True)
    first_name = models.CharField(_('Prenom'), max_length=30, blank=False)
    middle_name = models.CharField(_('middle name'), max_length=30, blank=True)
    last_name = models.CharField(_('Nom'), max_length=30, blank=False)
    #groups = models.ForeignKey(Group, on_delete=models.CASCADE,null=True)
    is_staff = models.BooleanField(_('staff status'), default=True,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
    is_active = models.BooleanField(_('active'), default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    def get_absolute_url(self):
        return "/users/%s/" % urlquote(self.username)

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

    def email_user(self, subject, message, from_email=None):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email])

    def get_profile(self):
        """
        Returns site-specific profile for this user. Raises
        SiteProfileNotAvailable if this site does not allow profiles.
        """
        warnings.warn("The use of AUTH_PROFILE_MODULE to define user profiles"
                      " has been deprecated.",
            PendingDeprecationWarning)
        if not hasattr(self, '_profile_cache'):
            from django.conf import settings
            if not getattr(settings, 'AUTH_PROFILE_MODULE', False):
                raise SiteProfileNotAvailable(
                    'You need to set AUTH_PROFILE_MODULE in your project '
                    'settings')
            try:
                app_label, model_name = settings.AUTH_PROFILE_MODULE.split('.')
            except ValueError:
                raise SiteProfileNotAvailable(
                    'app_label and model_name should be separated by a dot in '
                    'the AUTH_PROFILE_MODULE setting')
            try:
                model = models.get_model(app_label, model_name)
                if model is None:
                    raise SiteProfileNotAvailable(
                        'Unable to load the profile model, check '
                        'AUTH_PROFILE_MODULE in your project settings')
                self._profile_cache = model._default_manager.using(
                                   self._state.db).get(user__id__exact=self.id)
                self._profile_cache.user = self
            except (ImportError, ImproperlyConfigured):
                raise SiteProfileNotAvailable
        return self._profile_cache


class Vendeur(Person):
    typePerson = models.CharField(max_length=200,blank=True,default='vendeur')
    telephone = models.CharField(max_length=200,blank=True)

class Client(Person):
    typePerson = models.CharField(max_length=200,blank=True,default='client')
    telephone = models.CharField(max_length=200,blank=True)

class Categorie(models.Model):
    nom_categorie = models.CharField('Nom', max_length=70, default='', blank=True)
    url_categorie = models.CharField('URL', max_length=70, default='', blank=True) #HKA 21.08.2016 this field is added for the url in welcome page
    def __unicode__(self): #HKA 03.09.2016 this function display the name of categorie in product insertion page
        return u'%s [%s]' % (self.nom_categorie, self.url_categorie)


class Produit (models.Model):
    ref_prod = models.CharField('Reference', max_length=70, default='', blank=True)
    cat_prod = models.ForeignKey(Categorie, on_delete=models.CASCADE) 
    des_prod = models.TextField('Description',max_length=200,null=True,blank=True)
    owner = models.CharField('Proprietaire', max_length=70,  blank=True)
    code_prod = models.CharField('Code Produit', max_length=70,  blank=True)
    #commande = models.ForeignKey(Commande, on_delete=models.CASCADE, blank=True,null=True) 
    prix_prod = models.FloatField('Prix',null=True)
    remise_prod = models.FloatField('Remise',null=True)
    image_prod = models.ImageField('Image',blank=True)
    bulletin_analyse = models.ImageField('bulletin analyse',blank=True,upload_to='polls/static/polls/images')
    def categorie_produit(self):
        return self.cat_prod.nom_categorie
    def __unicode__(self): #HKA 03.09.2016 this function display the name of categorie in product insertion page
        return u'%s ' % (self.ref_prod)
    





class Panier(models.Model):
    id_clt = models.ForeignKey(Client, on_delete=models.CASCADE)
    ref_prod = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite_produit = models.IntegerField()
    def reference_produit(self):
        return self.ref_prod.ref_prod
   

class Facture (models.Model):
    id_clt = models.ForeignKey(Client, on_delete=models.CASCADE)
    #id_cmde = models.ForeignKey(Commande, on_delete=models.CASCADE)
    montant_fact = models.CharField('Montant Facture',max_length=200)
    owner = models.CharField('Proprietaire', max_length=70,  blank=True)


class MessageContact(models.Model):
    num_msg = models.CharField(max_length=200,null=True)
    #login_clt = 
    objet = models.CharField('Objet',max_length=200,null=True)
    contenu = models.TextField('Contenu',max_length=200,null=True)
    tel = models.CharField('Tel',max_length=200,null=True)
    email = models.CharField('Email',max_length=200,null=True)
    date_msg = models.DateTimeField('Date Message',auto_now_add=True,null=True)


