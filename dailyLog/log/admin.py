from django.contrib import admin

# Register your models here

from .models import Habit, Log

admin.site.register(Habit)
admin.site.register(Log)