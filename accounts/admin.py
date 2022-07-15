from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "username",
        "email",
        "shift",
        "badge",
        "is_staff",
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("shift", "badge")}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("shift", "badge")}),)


admin.site.register(CustomUser, CustomUserAdmin)
