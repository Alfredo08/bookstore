from django.contrib import admin

# Import the class/model
from .models import Customer

# Register your models here to see them in Django admin.
admin.site.register(Customer)