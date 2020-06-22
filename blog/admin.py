from django.contrib import admin

# Register your models here.
from .models import Blog #the class name in models.py

admin.site.register(Blog)
