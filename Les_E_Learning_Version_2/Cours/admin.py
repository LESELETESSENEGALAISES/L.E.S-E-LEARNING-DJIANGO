from django.contrib import admin
from .models import *

# Register your models here.


admin.site.site_header =  "LES-E-LEARNING ADMIN"


class NiveauAdmin(admin.ModelAdmin):
    list_display = ("niveau", "photo")

class CoursAdmin(admin.ModelAdmin):
    list_display = ("titre", "categorie", "photo", "niveau")
    

class Documents_CoursAdmin(admin.ModelAdmin):
    list_display = ("nom", "format_fichier", "fichier", "cours")
    
class CoursFeedbackAdmin(admin.ModelAdmin):
    list_display = ("feedback", "membre", "cours", "date")
    
class Membre_CoursAdmin(admin.ModelAdmin):
    list_display = ("membre", "cours")
    
# class LikeCoursAdmin(admin.ModelAdmin):
#     list_display = ("membre", "cours")
    
    
    
admin.site.register(Cours, CoursAdmin)
admin.site.register(CoursFeedback, CoursFeedbackAdmin)
admin.site.register(Niveau, NiveauAdmin)
admin.site.register(Membre_Cours, Membre_CoursAdmin)
admin.site.register(Documents_Cours ,Documents_CoursAdmin )
# admin.site.register(LikeCours)