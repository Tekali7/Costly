from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse
from .models import Expense

# Create your views here.

def index(request):
    expenses = Expense.objects.all()

    return render(request,
    "expense/index.html", {
    "expenses": expenses
    })