README
======

# About SNP ANALYZER:
<h3><em>A SNP navigation website created using Django framework.</em></h3>
<br>
<img src="snpapp/static/img/homelogo.png">
<br>

**Install all the needed dependencies**

```bash
cd ~/Desktop/projectsnp
pip install -r requirements.txt

```

**Import data and populate the databases in any case**
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py importData gwas_catalog.csv
./manage.py makemigrations snpapp
./manage.py migrate snpapp

```

**Start the App**
```bash
python manage.py runserver

```

# Author
CHERIF Aimen
