from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UserIntrest
from django.utils.translation import gettext_lazy as _

class CustomUserAdmin(UserAdmin):
    model = User

    # Display additional fields in user change form
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('username', 'first_name', 'last_name')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important datess'), {'fields': ('last_login', 'date_joined')}),
        # Add your custom fields here
        (_('Custom fields'), {'fields': ('email_confirmed', 'image', 'favorite', 'recently_viewed_chapters', 'saved_novels', 'last_searched', 'has_interest',  )}),
    )

    # Define the fields for the user creation form
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', ),
        }),
    )



# Register your models here.
admin.site.register(User)
admin.site.register(UserIntrest)