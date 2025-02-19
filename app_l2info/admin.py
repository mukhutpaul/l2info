from django.contrib import admin
from .models import Promotion,Etudiant

# Register your models here.

admin.site.register(Promotion,list_display=('codeprom','libelle'))
admin.site.register(Etudiant,list_display=('matricule','nom','postnom','promotion'),search_fields=['matricule','nom','postnom'])