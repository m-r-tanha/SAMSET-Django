# SAMSET-Django
<p> <h3> This is a startup project and I am going to run a Webscraping-NLP system to help someone who looks for a job. I have very innovative plans and I will use to the Data Science technologies in this project.
This project is in the first step, but finally, it will be appeared as a website, on this page I try to share and mention my challenges and my finding solution to cope with.
<h4>
<h2> Issue and solution when I am developing this Django site up
<h4> 
   
   
- Access to the admin webpage: (http://127.0.0.1:8009/admin/)
  - Create an account -->(python manage.py createsuperuser)
- Manage the next pages by adding them to admin.py

![Image of Yaktocat](https://github.com/m-r-tanha/SAMSET-Django/blob/master/admin.png)
  
- When I want to import models to insert data in data base (from models import *) this erros appear:
    django.core.exceptions.ImproperlyConfigured: Requested setting INSTALLED_APPS, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.
  - solution: 
        set DJANGO_SETTINGS_MODULE=samset.settings
        set DJANGO_SETTINGS_MODULE=settings
  - As a matter of fact, the above commands didn't help me, and I found I should run the (from models import *) in django shell
              	:pensive:    " python manage.py shell"

