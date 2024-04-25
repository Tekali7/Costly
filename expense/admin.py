from django.contrib import admin
from .models import Expense

# Register your models here.
"""
Registers the Expense model with the Django admin site.

**Model**: :model:`Expense`
"""
admin.site.register(Expense)
