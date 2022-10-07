from django.db import models

class SNP(models.Model):
    rsid = models.IntegerField(primary_key=True)
    chromosome_number = models.IntegerField()
    chromosome_pos = models.IntegerField()

    def __str__(self):
        return "rsid: " +self.rsid


class Reference(models.Model):
    pubmed_id = models.IntegerField(primary_key=True)
    journal = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return "pubmed id: " + self.pubmed_id

class Disease_Trait(models.Model):
    name = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return "disease: " +self.name


class SNP_Phenotype_Reference(models.Model):
    snp_rsid = models.ForeignKey(SNP, on_delete=models.CASCADE)
    reference_id = models.ForeignKey(Reference, on_delete=models.CASCADE)
    disease_trait = models.ForeignKey(Disease_Trait, on_delete=models.CASCADE)
    pvalue = models.FloatField()
    neglog10pvalue = models.FloatField()

    def __str__(self):
        return "rsid: " + self.snp_rsid + " disease: " + self.disease_trait + " pubmed id: " + self.reference_id
