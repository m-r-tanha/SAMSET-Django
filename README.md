# SAMSET-Django
This project is in first step, but it will be appeared as webpage
<h2> admin
   <h4>Access to the admin part of the site by address : (http://127.0.0.1:8009/admin/)
   <h4> at first we need a Username and Password:
      <h4> python manage.py createsuperuser
         <h4> the we shoud create this page in admin.py with adding the below commands
               <h3> at first we need a Username and Password:
      <h4> python manage.py createsuperuser
         <h4> the we shoud create this page in admin.py	
![Image of Yaktocat](https://github.com/m-r-tanha/SAMSET-Django/blob/master/admin.png)


<h2> Issue and solution when I am developing this Django site up
   <p>
    <h3> issue 1: 
       <h4> when I want to import models to insert data in data base (from models import *) this erros appear:
    django.core.exceptions.ImproperlyConfigured: Requested setting INSTALLED_APPS, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.
     <h4> solution: 
        <h5>(Django) C:\ProgramData\Anaconda3\envs\Django\Scripts\samset>set DJANGO_SETTINGS_MODULE=samset.settings
        <h5>(Django) C:\ProgramData\Anaconda3\envs\Django\Scripts\samset>set DJANGO_SETTINGS_MODULE=settings
           <h5> As a matter of fact, the above commands didn't help me, and I found I should run the (from models import *) in django shell
              	:pensive:    " python manage.py shell"
     </p>
