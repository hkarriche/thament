@python_2_unicode_compatible  # only if you need to support Python 2
class Client(models.Model):
    #id_clt = models.CharField(max_length=200)
    nom_clt = models.CharField(max_length=200)
    prenom_clt = models.CharField(max_length=200)
    adrs_clt = models.CharField(max_length=200)
    num_tel_clt = models.CharField(max_length=200)
    email_clt = models.CharField(max_length=200)
    login_clt = models.CharField(max_length=200)

    def __str__(self):
        return self.nom_clt
# @python_2_unicode_compatible  # only if you need to support Python 2
# class Vendeur(models.Model):
#     #id_clt = models.CharField(max_length=200)
#     nom_vend = models.CharField(max_length=200)
#     prenom_vend = models.CharField(max_length=200)
#     adrs_vend = models.CharField(max_length=200)
#     num_tel_vend = models.CharField(max_length=200)
#     email_vend = models.CharField(max_length=200)
#     login_vend = models.CharField(max_length=200)
#     def __str__(self):
#         return self.nom_vend
# @python_2_unicode_compatible  # only if you need to support Python 2
# class Administrateur(models.Model):
#     #id_clt = models.CharField(max_length=200)
#     nom_admin = models.CharField(max_length=200)
#     prenom_admin = models.CharField(max_length=200)
#     adrs_admin = models.CharField(max_length=200)
#     num_tel_admin = models.CharField(max_length=200)
#     email_admin = models.CharField(max_length=200)
#     login_admin = models.CharField(max_length=200)
#     def __str__(self):
#         return self.nom_admin

# class Categorie(models.Model):
#     nom_cat = models.CharField(max_length=200)

# class Produit(models.Model):
#     ref_prod = models.CharField(max_length=200)
#     cat_prod = models.ForeignKey(Categorie, on_delete=models.CASCADE)
#     desg_prod = models.CharField(max_length=200)
#     image_prod = models.CharField(max_length=200)





# class Panier(models.Model):
#     id_clt = models.ForeignKey(Client, on_delete=models.CASCADE)
#     ref_prod = models.ForeignKey(Produit, on_delete=models.CASCADE)
#     quantite_produit = models.IntegerField(max_length=200)


# class Commande(models.Model):
#     id_clt = models.ForeignKey(Client, on_delete=models.CASCADE)
#     ref_prod = models.ForeignKey(Produit, on_delete=models.CASCADE)
#     date_cmde = models.DateTimeField('date published')

# class Facture (models.Model):
#     id_clt = models.ForeignKey(Client, on_delete=models.CASCADE)
#     id_cmde = models.ForeignKey(Commande, on_delete=models.CASCADE)
#     montant_fact = models.CharField(max_length=200)


# class Message(models.Model):
#     login_clt = models.ForeignKey(Client, on_delete=models.CASCADE)
#     objet_msg = models.CharField(max_length=200)
#     contenu_msg = models.CharField(max_length=200)
#     date_msg = models.CharField(max_length=200)


