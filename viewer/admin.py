from django.contrib import admin

# Register your models here.

from .models import Company, Recruit

admin.site.register(Company)
admin.site.register(Recruit)
