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


# Add an expense
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


# Edit an expense
def edit_expense(request, expense_id):
    expense = get_object_or_404(Expense, pk=expense_id)

    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = ExpenseForm(instance=expense)

    context = {
        'form': form,
        'expense_id': expense_id
    }
    
    return render(request, 'edit_expense.html', context)