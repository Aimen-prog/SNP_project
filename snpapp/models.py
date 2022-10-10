from django.db import models

class SNP(models.Model):
    id = models.IntegerField(primary_key=True)
    chromosome_number = models.IntegerField()
    chromosome_pos = models.IntegerField()
    rsid = models.IntegerField(unique=True)
    def __str__(self):
        return "rsid: " + str(self.rsid)


class Reference(models.Model):
    id = models.IntegerField(primary_key=True)
    pubmed_id = models.IntegerField(unique=True)
    journal = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return "pubmed id: " + str(self.pubmed_id)

class Disease_Trait(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return "disease: " + self.name


class SNP_Phenotype_Reference(models.Model):
    id = models.IntegerField(primary_key=True)
    snp_id = models.ForeignKey(SNP, on_delete=models.CASCADE)
    reference_id = models.ForeignKey(Reference, on_delete=models.CASCADE)
    disease_trait_id = models.ForeignKey(Disease_Trait, on_delete=models.CASCADE)
    pvalue = models.FloatField()
    neglog10pvalue = models.FloatField()
