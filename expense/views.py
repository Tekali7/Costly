from django.shortcuts import render
from django.http import HttpResponse
from .models import Expense

# Create your views here.

def index(request):
    expenses = Expense.objects.all()

    return render(request,
    "index.html", {
    "expenses": expenses
    })