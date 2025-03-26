from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = [
        "username",
        "email",
    ]
    # Edit form configuration
    fieldsets = (
        (None, {'fields': ('username', 'email',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )

    # Add form configuration
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email',),
        }),
    )


admin.site.unregister(User)

admin.site.register(User, CustomUserAdmin)
