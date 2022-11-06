"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from snpapp import views as v
from django.contrib.auth import views as auth
from .router import router
from rest_framework.authtoken import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token, name='api-tokn-auth'),

    path('', include('snpapp.urls')),
    path('login/', v.Login, name='login'),
    path('logout/', auth.LogoutView.as_view(template_name='snpapp/home.html'), name='logout'),
    path('register/', v.register, name='register'),
    re_path(r'^phenotype_search/$', v.phenotype_search, name='phenotype_search'),
    re_path(r'^phenotype_list/$', v.phenotype_list, name='phenotype_list'),
    path('phenotype_selected/<str:disease_id>', v.phenotype_selected, name='phenotype_selected'),
    re_path(r'^snp_search/$', v.snp_search, name='snp_search'),
    path('snp_selected/<str:rs_id>/<str:ref_id>', v.snp_selected, name='snp_selected'),


]
