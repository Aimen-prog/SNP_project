# Generated by Django 2.2.13 on 2022-11-03 21:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disease_Trait',
            fields=[
                ('name', models.CharField(max_length=300, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('pubmed_id', models.IntegerField(primary_key=True, serialize=False)),
                ('journal', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='SNP',
            fields=[
                ('rsid', models.CharField(max_length=300, primary_key=True, serialize=False)),
                ('chromosome_number', models.CharField(max_length=15)),
                ('chromosome_pos', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SNP2Phenotype2Ref',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pvalue', models.FloatField(default=0)),
                ('neglog10pvalue', models.FloatField(default=0)),
                ('disease_trait', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='snpapp.Disease_Trait')),
                ('reference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='snpapp.Reference')),
                ('snp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='snpapp.SNP')),
            ],
        ),
    ]
