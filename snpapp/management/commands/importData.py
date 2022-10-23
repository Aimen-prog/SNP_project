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
        reader = csv.reader(open(path, encoding='utf-8'), delimiter='\t', quotechar='"')
        next(reader)
        for row in reader:
            if not row:
                continue  # skip empty lines
            snip = SNP()
            snip.rsid = row[21]
            snip.chromosome_number = row[11]
            snip.chromosome_pos = row[12]


            snip.save()

        # reader2 = csv.reader(open(path, encoding='utf-8'), delimiter='\t', quotechar='"')
        # next(reader2)
        # for row in reader2:
        #     reference = Reference()
        #     reference.pubmed_id = row[1]
        #     reference.journal = row[4]
        #     reference.title = row[6]
        #     reference.date = row[3]
        #     reference.save()
        #
        # reader3 = csv.reader(open(path, encoding='utf-8'), delimiter='\t', quotechar='"')
        # next(reader3)
        # for row in reader3:
        #     phenotype = Disease_Trait()
        #     phenotype.name = row[7]
        #     phenotype.save()
        #
        #
        # reader4 = csv.reader(open(path, encoding='utf-8'), delimiter='\t', quotechar='"')
        # next(reader4)
        # for row in reader4:
        #     all = SNP_Phenotype_Reference()
        #     all.pvalue = row[27]
        #     all.neglog10pvalue = row[28]
        #     all.save()
        #
        return HttpResponse("<h1>data imported successfully!</h1>")

