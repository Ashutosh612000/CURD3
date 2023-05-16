from django.contrib import admin
from myapp.models import Myapp_Detail

class Myapp_admin(admin.ModelAdmin):
    model = Myapp_Detail
    list_display = ['name','mobile','email','age']

admin.site.register(Myapp_Detail,Myapp_admin)
