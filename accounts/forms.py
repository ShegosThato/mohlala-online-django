from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Customer

#form for the signup page
class RegisterForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Customer
        fields = ('first_name', 'last_name', 'email', 'username', 'id_number', 'contact_info')
    

#forms for admin panel
class CustomerCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Customer
        fields = ('email', 'username', 'first_name', 'last_name', 'id_number')


class CustomerChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = Customer
        fields = UserChangeForm.Meta.fields
