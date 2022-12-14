from django.db import models


class SNP(models.Model):
    rsid = models.CharField(max_length=300, primary_key=True)
    chromosome_number = models.CharField(max_length=15)
    chromosome_pos = models.CharField(max_length=200)

    def __str__(self):
        return "rsid: " + self.rsid


class Reference(models.Model):
    pubmed_id = models.IntegerField(primary_key=True)
    journal = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    date = models.DateField()


    def __str__(self):
        return "pubmed id: " + str(self.pubmed_id)


class Disease_Trait(models.Model):
    name = models.CharField(max_length=300, primary_key=True)

    def __str__(self):
        return "disease/trait: " + self.name


class SNP2Phenotype2Ref(models.Model):
    snp = models.ForeignKey(SNP, on_delete=models.CASCADE)
    reference = models.ForeignKey(Reference, on_delete=models.CASCADE)
    disease_trait = models.ForeignKey(Disease_Trait, on_delete=models.CASCADE)
    pvalue = models.FloatField(default=0)
    neglog10pvalue = models.FloatField(default=0)

    def __str__(self):
        return "P-value: " + self.pvalue + "-log(P-value): " + self.neglog10pvalue