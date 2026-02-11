from django.contrib import admin
from .models import Book, School, User

# Register your models here.

admin.site.register(User)
admin.site.register(Book)
admin.site.register(School)
