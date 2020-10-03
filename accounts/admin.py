from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomerCreationForm, CustomerChangeForm
from .models import Customer


class CustomerAdmin(UserAdmin):
    add_form = CustomerCreationForm
    form = CustomerChangeForm
    list_display = ['email', 'username', 'first_name', 'last_name', 'id_num']
    model = Customer

admin.site.register(Customer, UserAdmin)

admin.site.site_header = "Mohlala Online"
admin.site.site_title = "Mohlala Portal"
admin.site.index_title = "Welcome to Mohlala Portal"
