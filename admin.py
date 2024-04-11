from django.contrib import admin
from .models import *

# Register your models here.

admin.site.site_header = 'Chaos Control Media'
admin.site.register(Task)
