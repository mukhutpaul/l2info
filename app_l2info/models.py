from django.db import models

# Create your models here.

class Promotion(models.Model):
    codeprom = models.CharField(max_length=10,primary_key=True)
    libelle = models.CharField(max_length=100)
    
    def __str__(self):
        return self.libelle
    
class Etudiant(models.Model):
    matricule = models.CharField(max_length=10,primary_key=True)
    nom = models.CharField(max_length=100,null=False)
    postnom = models.CharField(max_length=100)
    sexe = models.CharField(max_length=1)
    telephone = models.CharField(max_length=15,unique=True)
    datenais = models.DateField()
    dateins = models.DateField(auto_now=True)
    poids = models.DecimalField(max_digits=3,decimal_places=2)
    promotion = models.ForeignKey(Promotion,on_delete=models.CASCADE)
    
