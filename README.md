# REST API Pizza order

simplified pizza ordering service using django REST and postgreSQL.

## Installation
1. create virtual environment:
> *virtualenv env --no-site-packages*

2. activate env:
> *env/scripts/activate*

3. install packages:
> *pip install -r requirements.txt*

## Run
1. create a database oder use the *pizzaDB.backup*
> *psql -U username -d pizzaDB -p 5432 -1 -f pizzaDB.backup*
2. create migrations and migrate
> *python manage.py makemigrations*
> *python mange.py migrate*
3. start developer server
> *python manage.py runserver*

*pizzaDB.backup* contains a backup of a postgreSQL database. If you use this database the username is 'admin' and the password is 'pizzaisgreat'.

Postgres Database:
> 'pizzaDB.backup' is a backup for postgres (version 10.).
> You have to create a new DB and restore 'pizzaDB.backup' in it. 
> Change name, user and password in 'settings.py'