from django.contrib import admin
from .models import WebInput
from .models import UserInsert

# Register your models here.

admin.site.register( WebInput )
admin.site.register(UserInsert)
