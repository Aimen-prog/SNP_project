import django_tables2 as tables
from .models import Disease_Trait


class PhenotypeTable(tables.Table):
    name = tables.Column()

    class Meta:
        model = Disease_Trait
        attrs = {'class': 'table table-striped table-hover'}

