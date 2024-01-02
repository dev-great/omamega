from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .forms import *
from .models import *


class CustomUserAdmin(admin.ModelAdmin):
    # add_form = UserAdminCreationForm
    # form = UserAdminChangeForm

    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        (_('Personal info'), {'fields': (
            'first_name', 'last_name', 'is_Landlord', 'is_Subscriber', 'address',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff',
         'is_superuser', 'groups', 'user_permissions',)}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ['email', 'first_name', 'last_name',
                    'is_staff', 'is_Landlord', 'is_Subscriber', 'address', 'phone_number']
    search_fields = ('email', 'first_name', 'last_name', 'phone_number',
                     'is_Landlord', 'is_Subscriber', 'address',)
    ordering = ('email',)

    # def get_form(self, request, obj=None, **kwargs):
    #     if obj is None:
    #         return self.add_form
    #     return super().get_form(request, obj, **kwargs)


admin.site.register(CustomUser, CustomUserAdmin)
