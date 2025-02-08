from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'phone_number', 'address', 'created_at', 'is_active')
    
admin.site.register(CustomUser, CustomUserAdmin)