from django.contrib import admin
from .models import *

admin.site.site_title = 'dashboard manage'
admin.site.sitee_header = ''


mymodels = [UserRole,Master,Student,Teacher,Book]

for model in mymodels:
    admin.site.register(model)
# Register your models here.
