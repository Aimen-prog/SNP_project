from django.db import models


class SNP(models.Model):
    rsid = models.CharField(max_length=300, primary_key=True)
    chromosome_number = models.CharField(max_length=5)
    chromosome_pos = models.IntegerField(default=0)  # add default=0 for empty string

    def __str__(self):
        return "rsid: " + self.rsid


class Reference(models.Model):
    pubmed_id = models.IntegerField(primary_key=True)
    journal = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return "pubmed id: " + str(self.pubmed_id)


class Disease_Trait(models.Model):
    name = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return "disease: " + self.name


class SNP_Phenotype_Reference(models.Model):
    snp_rsid = models.ForeignKey(SNP, on_delete=models.CASCADE)
    reference_id = models.ForeignKey(Reference, on_delete=models.CASCADE)
    disease_trait = models.ForeignKey(Disease_Trait, on_delete=models.CASCADE)
    pvalue = models.FloatField()
    neglog10pvalue = models.FloatField()


