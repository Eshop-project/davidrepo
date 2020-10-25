# Code Structure


## App Settings

tree eShop
    
    .
    ├── web_design
    │   ├── admin.py
    │   ├── apps.py
    │   ├── migrations
    │   ├── models.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── eShop
    │   ├── asgi.py
    │   ├── settings.py
    │   └── wsgi.py
    ├── templates
    ├── db.sqlite3
    └── manage.py


The [settings.py] file runs the app startup.

This is in the "web_design" app folder.

Startup files are "asgi.py" and "wsgi.py" and "manage.py".

Data migrations folder contains all the database migration history.

## HTML Templates

* All HTML template files are located in "templates" folder
