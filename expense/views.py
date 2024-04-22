from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from django import forms
from .models import Expense
from .forms import ExpenseForm

# Create your views here.

@login_required
def index(request):
    expenses = Expense.objects.filter(user=request.user)

    return render(request,
    "expense/index.html", {
    "expenses": expenses
    })


@login_required
def add_expense(request):
    if request.method == 'POST':
        expense_form = ExpenseForm(data=request.POST)
        if expense_form.is_valid():
            expense = expense_form.save(commit=False)
            expense.user = request.user
            expense.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Expense added successfully!'
            )
            return redirect('index')
    else:
        expense_form = ExpenseForm()

    return render(request, 'expense/add_expense.html', {'expense_form': expense_form})