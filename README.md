# SAMSET-Django
This project is in first step, but it will be appeared as webpage
<h2> Issue and solution when I am geveloping this Django site up
   <p>
    <h3> issue 1: 
       <h4> when I want to import models to insert data in data base (from models import *) this erros appear:
    django.core.exceptions.ImproperlyConfigured: Requested setting INSTALLED_APPS, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.
     <h4> solution: 
        <h5>(Django) C:\ProgramData\Anaconda3\envs\Django\Scripts\samset>set DJANGO_SETTINGS_MODULE=samset.settings
        <h5>(Django) C:\ProgramData\Anaconda3\envs\Django\Scripts\samset>set DJANGO_SETTINGS_MODULE=settings
     </p>
