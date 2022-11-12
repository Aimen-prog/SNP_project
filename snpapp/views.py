from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_exempt
from .forms import UserRegisterForm, phenotype_search_form, snp_search_form, snp_search_nbr_form
from .models import Disease_Trait, SNP2Phenotype2Ref, Reference, SNP
from django.db.models import F



def home(request):
    return render(request, 'snpapp/home.html', {'title': 'home'})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'snpapp/register.html', {'form': form,'title':'Register'})


def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' Welcome {username}!')
            return redirect('home')
        else:
            messages.info(request, f'Account does not exist')
    form = AuthenticationForm()
    return render(request, 'snpapp/login.html', {'form':form,'title':'Log in'})




@login_required
def phenotype_search(request):
    if request.method == "POST":
        form = phenotype_search_form(request.POST)
        if form.is_valid():
            # join SNP2Pheno2Ref and Reference tables to get information about phenotype
            joinData = SNP2Phenotype2Ref.objects.select_related('reference')\
                .annotate(journal=F('reference__journal') ,title=F('reference__title'), date=F('reference__date') )\
                .values('snp_id', 'reference_id', 'disease_trait_id','pvalue','neglog10pvalue','journal','title', 'date')\
                .filter(disease_trait_id=form.cleaned_data['my_phenotype'])
            return render(request, 'snpapp/phenotype_detail.html', {'posts': joinData})
    else:
        form = phenotype_search_form()
        all_pheno = Disease_Trait.objects.all()
    return render(request, 'snpapp/phenotype_search.html', {'form': form, "phenotypes": all_pheno})

@login_required
def phenotype_list(request):
    all_pheno = Disease_Trait.objects.all()
    return render(request, 'snpapp/phenotype_list.html', {'posts': all_pheno})

@login_required
@csrf_exempt
def phenotype_selected(request, disease_id):
        disease = SNP2Phenotype2Ref.objects.select_related('reference') \
            .annotate(journal=F('reference__journal'), title=F('reference__title'), date=F('reference__date')) \
            .values('snp_id', 'reference_id', 'disease_trait_id', 'pvalue', 'neglog10pvalue', 'journal', 'title', 'date') \
            .filter(disease_trait_id=disease_id)
        return render(request, 'snpapp/phenotype_detail.html', {'posts': disease})


@login_required
def snp_search(request):
    if request.method == "POST":
        form = snp_search_form(request.POST)
        if form.is_valid():
            # join SNP2Pheno2Ref and SNP tables to get information about snp
            joinData = SNP2Phenotype2Ref.objects.select_related('snp')\
                .annotate(chrom=F('snp__chromosome_number') , pos=F('snp__chromosome_pos'))\
                .values('snp_id', 'reference_id', 'disease_trait_id','pvalue','neglog10pvalue','chrom','pos')\
                .filter(snp_id=form.cleaned_data['my_snp'])
            return render(request, 'snpapp/snp_results.html', {'posts': joinData})
    else:
        form = snp_search_form()
        all_snp = SNP.objects.all()
    return render(request, 'snpapp/snp_search.html', {'form': form, "snps": all_snp})

@login_required
@csrf_exempt
def snp_selected(request, rs_id, ref_id):
        snp = SNP2Phenotype2Ref.objects.select_related('snp','reference')\
                .annotate(chrom=F('snp__chromosome_number') , pos=F('snp__chromosome_pos'),journal=F('reference__journal'),
                          title=F('reference__title'), date=F('reference__date') )\
                .values('snp_id', 'reference_id', 'disease_trait_id','pvalue','neglog10pvalue','chrom','pos', 'journal', 'title', 'date')\
                .filter(snp_id=rs_id).filter(reference_id=ref_id)
        return render(request, 'snpapp/snp_detail.html', {'posts': snp})


@login_required
def snp_search_nbr(request):
    if request.method == "POST":
        form = snp_search_nbr_form(request.POST)
        if form.is_valid():
            joinData = SNP2Phenotype2Ref.objects.select_related('snp')\
                .annotate(chrom=F('snp__chromosome_number') , pos=F('snp__chromosome_pos'))\
                .values('snp_id', 'reference_id', 'disease_trait_id','pvalue','neglog10pvalue','chrom','pos')\
                .filter(chrom=form.cleaned_data['chr'])
            return render(request, 'snpapp/snp_results.html', {'posts': joinData})
    else:
        form = snp_search_nbr_form()
        all_snp = SNP.objects.all()
    return render(request, 'snpapp/snp_search_nbr.html', {'form': form, "snps": all_snp})



