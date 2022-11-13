README
======

# About SNP ANALYZER:
<h3><em>A SNP navigation website created using Django framework.</em></h3>
  <a href="https://github.com/Aimen-prog/">
    <img src="snpapp/static/img/homelogo.png" alt="Logo" >
  </a>

<h2>Install all the needed dependencies</h2>
```bash
cd ~/Desktop/projectsnp
pip install -r requirements.txt
```

<h2>Import data and populate the databases in any case</h2>
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py importData gwas_catalog.csv
./manage.py makemigrations snpapp
./manage.py migrate snpapp
```

<h2>Start the App</h2>
```bash
python manage.py runserver
```
# Author
CHERIF Aimen
