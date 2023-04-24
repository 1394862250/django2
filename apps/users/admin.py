from django.contrib import admin

# Register your models here.

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'display_name', 'email', 'is_staff', 'is_active', 'last_login')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('username', 'display_name', 'email')
