from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm




class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class phenotype_search_form(forms.Form):
    my_phenotype = forms.CharField(label='Phenotype name*', required=True)
    my_phenotype.widget = forms.TextInput(attrs={'id': 'tags', })

class snp_search_form(forms.Form):
    my_snp = forms.CharField(label='Snp Rsid*', required=True)
    my_snp.widget = forms.TextInput(attrs={'id': 'snptags', })


class snp_search_nbr_form(forms.Form):
    chr = forms.CharField(label='Chromosome number*', required=True)
    chr.widget = forms.TextInput(attrs={'id': 'chrtags', })


class snp_search_pos_form(forms.Form):
    start = forms.IntegerField(label='Chromosome position start*', required=True)
    end = forms.IntegerField(label='Chromosome position end*', required=True)

    chr = forms.CharField(label='Chromosome number (optional)', required=False)
    chr.widget = forms.TextInput(attrs={'id': 'chrtags', })















