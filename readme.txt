create virtual environment:
    $ virtualenv env --no-site-packages

activate env:
    $ env/scripts/activate

install packages:
    $ pip install -r requirements.txt

admin login:
    admin
    pizzaisgreat

Postgres Database:
    'pizzaDB.backup' is a backup for postgres (version 10.).
    You have to create a new DB and restore 'pizzaDB.backup' in it. 
    Change name, user and password in 'settings.py'

API testing:
    $ python manage.py runserver
    $ python api_test.py
    --> a result of API testing is stored in 'api_testing_protocol.txt'