from django.urls import path
from . import views

urlpatterns = [
    path("expense/", views.index, name="index"),
    path("add_expense/", views.add_expense, name="add_expense"),
   # path("delete_expense/", views.delete_expense, name="delete_expense"),
   # path("edit_expense/", views.edit_expense, name="edit_expense")
]