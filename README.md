**framework component
- MODEL - defines a logical data structure and is the data handler between thte database and the view
- TEMPLATE - is sort of the presentation layer, Django uses plain-text template system that keeps everything that the browser renders
- VIEWS - communicates with the database via the model and transfers the data to the template for viewing
- CONTROLLER - the framework itself acts as the controller, sending request to the appropriate view, according to the Django URL configurations

- HOW DJANGO HANDLES HTTP REQUEST AND HANDLES RESPONSE
1 . A web browser makes a http request for a webpage by its URL and the web server passes the HTTP request to Django
2. Django runs through its configured URL patterns and stops at the first one that matches the requested URL.
3. Django executes the view that corresponds to the matched URL pattern.
4. the view potentially uses data models to retrieve information from the database
5. The Data Models provide data definitions and behaviours. They are used to query the database
6. The view renders a template (usually HTML) to display the data and returns it with an HTTP response

NOTE: django also includes HOOKS in the request/response process, which is called MIDDLEWARE. 

- the project in this directory is a blog site
- om initilization of a django-project the following are the project structure
>> django-admin startproject blogsite
blogsite/
   manage.py
   blogsite/
         __init__.py
         asgi.py
         settings.py
         urls.py
         wsgi.py

manage.py - is a command line utility for interacting with the terminal, no edits needed here
blosgsite/ - this is the inner directory and the python package for the project containing some files such as:
   - __init__.py - an empty file that tells python to treat the mysite/ as a module
   - asgi.py - a config file that runs the project as an ASGI app, with ASGI compactible webserver. ASYNCHRONOUS SERVER GATEWAY INTERFACE
   - settings.py - settings and config files for my project, with default settings, some config edits needed here while building
   - urls.py - URL patterns live here, mapped to a view
   - wsgi.py - WEB SERVER GATEWAY INTERFACE, config file that runs the project as a wsgi app with compactible wsgi webserver

   a compactible lite-weight database that comes bundled with python3,and is listed in DATABASE settings in the settings.py, used for development purposes is the default SQLITE. in production  a full-featured database is required like postgres, mysql of oracle.

To complete the project setup, you need to create the 
tables associated with the models of the default Django applications included in the INSTALLED_APPS
setting. Django comes with a system that helps you manage database migrations.
>> cd blog
>> python manage.py migrate

The preceding lines are the database migrations that are applied by Django. By applying the initial migrations, the tables for the applications listed in the INSTALLED_APPS setting are created in the database.

- RUNNING DEVEOPMENT SERVER
Django comes with a lightweight web server to run your code quickly, without needing to spend time 
configuring a production server. When you run the Django development server, it keeps checking 
for changes in your code. It reloads automatically, freeing you from manually reloading it after code 
changes. However, it might not notice some actions, such as adding new files to your project, so you 
will have to restart the server manually in these cases.
Start the development server by typing the following command in the shell prompt:
>> python manage.py runserver

💡: You can run the Django development server on a custom host and port or tell Django to load a specific 
settings file, as follows:
>> python manage.py runserver 127.0.0.1:8001 --settings=blog.settings.py
this operation comes in handly When you have to deal with multiple environments that require different configurations, 
you can create a different settings file for each environment.

💡: This server is only intended for development and is not suitable for production use. To deploy Django 
in a production environment, you should run it as a WSGI application using a web server, such as 
Apache, Gunicorn, or uWSGI, or as an ASGI application using a server such as Daphne or Uvicorn. 
You can find more information on how to deploy Django with different web servers at https://docs.
djangoproject.com/en/5.0/howto/deployment/wsgi/.

PROJECT SETTINGS:
There are several 
settings that Django includes in this file, but these are only part of all the available Django settings. 
You can see all the settings and their default values at https://docs.djangoproject.com/en/5.0/
ref/settings/.

DJANGO PROJECT / DJANGO APP
. In Django, 
a project is considered a Django installation with some settings. An application is a group of models, 
views, templates, and URLs. Applications interact with the framework to provide specific functionalities and may be reused in various projects. You can think of a project as your website, which contains 
several applications, such as a blog, wiki, or forum, that can also be used by other Django projects.

DJANGO_PROJECT
   |
   | -- APP 1 (blog)
   |
   | -- APP 2 (chat)
   |
   | -- APP 3 (wiki)
   \

CREATNG AN APP
inside the django project directory enter the command
>> python manage.py startapp myblogsite

it will create an app directory inside the django project directory called myblogsite with some set of file and directories like this at the start of the django app on default

blog\
   blog\
  *myblogsite\
      __init__.py
      admin.py
      apps.py
      models.py
      test.py
      views.py
      migrations\
         __init__.py

- __init__py - empty on starting to tell python to treat the blog directory as a python module
- admin.py - register models here to include them in the django admin site - using this is optional
- apps.py - Main config of the blogsite app
- migrations\ -directory contain  database migrations allowing django to track model changes and sync the DB Accordingly, it contains at empty __int__.py file on default
- models.py - includes data models of myblogsite app.
- test.py - test for the app can be added here
- views.py - app logic goes here, functions tjhat describes how views receive http request and how they process and route a response

