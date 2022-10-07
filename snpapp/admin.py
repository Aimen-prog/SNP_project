from django.contrib import admin
from .models import SNP, Reference, Disease_Trait, SNP_Phenotype_Reference

admin.site.register(SNP)
admin.site.register(Reference)
admin.site.register(Disease_Trait)
admin.site.register(SNP_Phenotype_Reference)
