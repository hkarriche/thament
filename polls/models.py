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



class AccountManager(BaseUserManager):

    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Must have an email address')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class VendorManager(BaseUserManager):

    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Must have an email address')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
class Client(AbstractBaseUser):
    email = models.EmailField('Email', unique=True, max_length=255)
    first_name = models.CharField('First Name', max_length=70, default='', blank=True)
    last_name = models.CharField('Last Name', max_length=70, default='', blank=True)
    full_name = models.CharField('Full Name', max_length=150, default='', blank=True)
    login = models.CharField('login', max_length=150, default='', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField('Is Active', default=True)
    is_staff = models.BooleanField('Is Staff', default=False, db_index=True)
    is_superuser = models.BooleanField('Is Superuser', default=False, db_index=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = AccountManager()

    class Meta:
        ordering = ['-modified']
        verbose_name_plural = 'Clients'

    def get_full_name(self):
        return self.full_name or "%s %s" % (self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name or self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

AbstractBaseUser._meta.get_field('password').verbose_name = _('password_client')

class Vendeur(AbstractBaseUser):
    email = models.EmailField('Email', unique=True, max_length=255)
    first_name = models.CharField('First Name', max_length=70, default='', blank=True)
    last_name = models.CharField('Last Name', max_length=70, default='', blank=True)
    full_name = models.CharField('Full Name', max_length=150, default='', blank=True)
    login = models.CharField('login', max_length=150, default='', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField('Is Active', default=True)
    is_staff = models.BooleanField('Is Staff', default=False, db_index=True)
    is_superuser = models.BooleanField('Is Superuser', default=False, db_index=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = VendorManager()

    class Meta:
        ordering = ['-modified']
        verbose_name_plural = 'Vendeurs'

    def get_full_name(self):
        return self.full_name or "%s %s" % (self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name or self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
AbstractBaseUser._meta.get_field('password').verbose_name = _('password_vendeur')

class Categorie(models.Model):
    nom_categorie = models.CharField(max_length=200)

class Produit (models.Model):
    ref_prod = models.CharField(max_length=200)
    cat_prod = models.ForeignKey(Categorie, on_delete=models.CASCADE) 
    des_prod = models.CharField(max_length=200) 
    prix_prod = models.FloatField(null=True)
    remise_prod = models.FloatField(null=True)
    image_prod = models.ImageField(upload_to='polls/images')

class Panier(models.Model):
    id_clt = models.ForeignKey(Client, on_delete=models.CASCADE)
    ref_prod = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite_produit = models.IntegerField()


class Commande(models.Model):
    id_clt = models.ForeignKey(Client, on_delete=models.CASCADE)
    ref_prod = models.ForeignKey(Produit, on_delete=models.CASCADE)
    date_cmde = models.DateTimeField()

class Facture (models.Model):
    id_clt = models.ForeignKey(Client, on_delete=models.CASCADE)
    id_cmde = models.ForeignKey(Commande, on_delete=models.CASCADE)
    montant_fact = models.CharField(max_length=200)


class MessageContact(models.Model):
    num_msg = models.CharField(max_length=200)
    #login_clt = 
    objet_msg = models.CharField(max_length=200)
    contenu_msg = models.CharField(max_length=200)
    date_msg = models.DateTimeField()







# class User(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(_('email address'), unique=True)
#     first_name = models.CharField(_('first name'), max_length=30, blank=True)
#     last_name = models.CharField(_('last name'), max_length=30, blank=True)
#     date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
#     is_active = models.BooleanField(_('active'), default=True)
#     avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)


@python_2_unicode_compatible  # only if you need to support Python 2
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    probability = models.IntegerField(default=0)

    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
@python_2_unicode_compatible  # only if you need to support Python 2
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


    def __str__(self):
        return self.choice_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
