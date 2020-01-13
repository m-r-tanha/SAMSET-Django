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

