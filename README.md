# SAMSET-Django
<p> <h3> This is a startup project and I am going to run a Webscraping-NLP system to help someone who looks for a job. I have some Data Science innovative plans and I will use then in this project.
This project is in infancy part, but at the end, it will be appeared as a website, on this page I try to share and mention my challenges/solution/experience to up a site.
<h4>
<h2> Issue and solution when I am developing this Django site up
<h4> 
   
   
- Access to the admin webpage: (http://127.0.0.1:8009/admin/)
  - Create an account -->(python manage.py createsuperuser)
- Manage the next pages by adding them to admin.py

![Image of Yaktocat](https://github.com/m-r-tanha/SAMSET-Django/blob/master/admin.png)
  
- When I want to import models to insert data to the data base (from models import *) this erros appear:
    django.core.exceptions.ImproperlyConfigured: Requested setting INSTALLED_APPS, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.
  - solution: 
        set DJANGO_SETTINGS_MODULE=samset.settings
        set DJANGO_SETTINGS_MODULE=settings
  - As a matter of fact, the above commands didn't help me, and I found, I should run the (from models import *) in django shell
              	:pensive:    " python manage.py shell"

## Most  Important Information about Django

 - open source web application framework.
 - Django follows Model-View-Template (MVT) architectural pattern.
 - Model: It is the data access layer. It contains everything about the data.
 - View: It is the business logic layer. This layer contains the logic that accesses the model and defers to the appropriate template.
 - Urls uses a regular expression to capture URL patterns for processing.
 - When a visitor lands on Django page, first Django checks the URLs pattern you have created and used the information to retrieve the view. After that view processes the request, querying your database if necessary, and passes the requested information to a template. After that, the template renders the data in a layout you have created and displayed the page.
 - Django is a high-level Python's web framework which was designed for rapid development and clean, realistic design.
 - Features available in Django web framework are:

      - Admin Interface (CRUD)
      - Templating
      - Form handling
      - Internationalization
      - A Session, user management, role-based permissions
      - Object-relational mapping (ORM)
      - Testing Framework
      - Fantastic Documentation
  - There are three possible inheritance styles in Django:
      - Abstract base classes: This style is used when you only want parent's class to hold information that you don't want to type out for each child model.
      - Multi-table Inheritance: This style is used if you are sub-classing an existing model and need each model to have its database table.
      - Proxy models: This style is used, if you only want to modify the Python level behavior of the model, without changing the model's fields.
   - Django is not a CMS (Content Management System). Instead, it is a Web framework and a programming tool that makes you able to build websites.
   - There are three main things required to set up static files in Django:
      - Set STATIC_ROOT in settings.py
      - run manage.py collect static
      - set up a Static Files entry on the web tab
      
   - Some usage of middlewares in Django is:
      - Session management,
      - Use authentication
      - Cross-site request forgery protection
      - Content Gzipping
      
   - A session is a mechanism to store information on the server side during the interaction with the web application.
   - An exception is an abnormal event that leads to program failure. To deal with this situation, Django uses its exception classes and supports all core Python exceptions as well. 
