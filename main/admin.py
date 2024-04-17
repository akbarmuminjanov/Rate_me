from django.contrib import admin
from .models import Register, Stars
# Register your models here.

@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ("username", "password")

@admin.register(Stars)
class StarsAdmin(admin.ModelAdmin):
    list_display = ("full_name", "view")