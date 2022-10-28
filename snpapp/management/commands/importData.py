import csv
import os.path
from django.core.management.base import BaseCommand
from snpapp.models import SNP, Reference, Disease_Trait, SNP2Phenotype2Ref
from django.core.exceptions import ObjectDoesNotExist


class Command(BaseCommand):
    help = 'Add data from a csv file to the database'

    def add_arguments(self, parser):
        parser.add_argument('file', type=str)

    def handle(self, *args, **options):

        directory = os.path.dirname(os.path.dirname(__file__))
        path = os.path.join(directory, 'data', options['file'])
        reader = csv.reader(open(path, encoding='utf-8'), delimiter='\t', quotechar='"')
        next(reader)
        for row in reader:
            # CREATE SNP TABLE
            try:
                stored_snp = SNP.objects.get(rsid=row[21])
            except ObjectDoesNotExist:
                snp = SNP.objects.create(
                    rsid=row[21],  #'SNPS'
                    chromosome_number=row[11], #'CHR_ID'
                    chromosome_pos=row[12] #'CHR_POS'
                )

            # CREATE REFERENCE TABLE
            try:
                stored_ref = Reference.objects.get(pubmed_id=row[1])
            except ObjectDoesNotExist:
                ref = Reference.objects.create(
                    pubmed_id=row[1],  #'PUBMEDID'
                    journal=row[4], #'JOURNAL'
                    title=row[6],  #'STUDY'
                    date=row[3]    #'DATE'
                )
            # CREATE DISEASE_TRAIT TABLE
            try:
                stored_trait = Disease_Trait.objects.get(name=row[7])
            except ObjectDoesNotExist:
                trait = Disease_Trait.objects.create(
                    name=row[7] #'DISEASE/TRAIT'
                )
            # CREATE SNP2Phenotype2Ref TABLE
            id_snip = SNP.objects.filter(rsid=row[21])  # 'SNPS'
            id_ref = Reference.objects.filter(pubmed_id=row[1])  # 'PUBMEDID'
            id_trait = Disease_Trait.objects.filter(name=row[7])  # 'DISEASE/TRAIT'

            if id_snip.exists() and id_ref.exists() and id_trait.exists():
                pvalue = SNP2Phenotype2Ref.objects.create(
                    reference=id_ref.first(),
                    disease_trait=id_trait.first(),
                    snp=id_snip.first(),
                    pvalue=row[27],  #'P-VALUE'
                    neglog10pvalue=row[28]  #'PVALUE_MLOG'
                )