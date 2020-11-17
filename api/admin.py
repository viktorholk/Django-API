from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import Node
# Register your models here.

class UserAdmin(UserAdmin):

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('node', 'created_at', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('node', 'password')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('node', 'created_at', 'password1', 'password2'),
        }),
    )
    search_fields = ('node',)
    ordering = ('node',)
    filter_horizontal = ()


admin.site.register(Node, UserAdmin)
admin.site.unregister(Group)