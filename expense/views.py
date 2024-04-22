from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from django import forms
from .models import Expense

# Create your views here.

@login_required
def index(request):
    expenses = Expense.objects.filter(user=request.user)

    return render(request,
    "expense/index.html", {
    "expenses": expenses
    })


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['item', 'amount', 'currency']


@login_required
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Expense added successfully!'
            )
            return redirect('index')
    else:
        form = ExpenseForm()
    return render(request, 'expense/add_expense.html', {'form': form})