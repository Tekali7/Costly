from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Expense

# Create your views here.

@login_required
def index(request):
    expenses = Expense.objects.filter(user=request.user)

    return render(request,
    "expense/index.html", {
    "expenses": expenses
    })