from django.contrib import admin
from .models import SNP, Reference, Disease_Trait, SNP_Phenotype_Reference

admin.site.register(SNP, Reference, Disease_Trait, SNP_Phenotype_Reference)