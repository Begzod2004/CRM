from django.contrib import admin
from .forms import *
from .models import *
from django.contrib.auth.admin import UserAdmin
class MyAdmin(UserAdmin):
    list_filter = ['role','is_active','is_staff','is_superuser']
    list_display = ['role','username','email','is_staff','is_superuser']


admin.site.register(User,MyAdmin)
class DirectorAdmin(UserAdmin):
    list_filter = ['role','is_active']
    model = Director
    add_form =DirectorForm


admin.site.register(Director,DirectorAdmin)
# #########################

class ManagerAdmin(UserAdmin):
    model = Manager
    add_form =ManagerForm
admin.site.register(Manager,ManagerAdmin)


