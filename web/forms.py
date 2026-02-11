from django import forms
from django.forms import ModelForm
from .models import Book, School, User
from django.contrib.auth.forms import UserCreationForm



class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class SchoolForm(ModelForm):
    class Meta:
        model = School
        fields = '__all__'

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()

class CreateUser(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'surname',
            'firstname',
            'middlename',
            'phone_number',
            'username',
            'email',
            'password1',
            'password2',
            'address',
        )
