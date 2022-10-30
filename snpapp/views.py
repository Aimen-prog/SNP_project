from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm, phenotype_search_form
from .models import Disease_Trait, SNP2Phenotype2Ref, Reference, SNP
from django_tables2 import SingleTableView
from .tables import (
    PhenotypeTable
)



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
            messages.success(request, f' Welcome {username} !')
            return redirect('home')
        else:
            messages.info(request, f'Account does not exist')
    form = AuthenticationForm()
    return render(request, 'snpapp/login.html', {'form':form,'title':'Log in'})




class ClassBased(SingleTableView):
    table_class = PhenotypeTable
    queryset = Disease_Trait.objects.all()
    template_name = "snpapp/phenotype_list.html"
class_based = ClassBased.as_view()

def search_phenotype(request):
    if request.method == "POST":
        form = phenotype_search_form(request.POST)
        if form.is_valid():
            joinData = SNP2Phenotype2Ref.objects.filter(disease_trait_id=form.cleaned_data['my_phenotype'])

            return render(request, 'snpapp/phenotype_detail.html', {'posts': joinData})
    else:
        form = phenotype_search_form()
    return render(request, 'snpapp/search_phenotype.html', {'form': form})



