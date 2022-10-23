import csv
import os.path
from django.http import HttpResponse
from django.core.management.base import BaseCommand, CommandError
from snpapp.models import SNP_Phenotype_Reference, SNP, Reference, Disease_Trait


class Command(BaseCommand):
    help = 'Add data from a csv file to the database'

    def add_arguments(self, parser):
        parser.add_argument('file', type=str)


    def handle(self, *args, **options):
        directory = os.path.dirname(os.path.dirname(__file__))
        path = os.path.join(directory, 'data', options['file'])
        #read the data file
        reader = csv.reader(open(path, encoding='utf-8'), delimiter='\t', quotechar='"')
        next(reader)
        for row in reader:
            snip = SNP()
            reference = Reference()
            phenotype = Disease_Trait()
            all = SNP_Phenotype_Reference()

            snip.rsid = row[21]
            snip.chromosome_number = row[11]
            snip.chromosome_pos = row[12]

            reference.pubmed_id = row[1]
            reference.journal = row[4]
            reference.title = row[6]
            reference.date = row[3]

            phenotype.name = row[7]


            all.snp_rsid = SNP.objects.get(str(row[21]))
            all.reference_id = Reference.objects.get(int(row[1]))
            all.disease_trait = Disease_Trait.objects.get(str(row[7]))
            all.pvalue = row[27]
            all.neglog10pvalue = row[28]

            all.save()
            phenotype.save()
            reference.save()
            snip.save()
        return HttpResponse("<h1>data imported successfully!</h1>")

