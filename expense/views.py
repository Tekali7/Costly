from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
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


def add_expense(request):
    if request.method == 'POST':
        form = forms.Form(request.POST)
        if form.is_valid():
            item = form.cleaned_data['item']
            amount = form.cleaned_data['amount']
            currency = form.cleaned_data['currency']
            if item and amount and currency:
                expense = Expense.objects.create(item=item, amount=amount, currency=currency, user=request.user)
                return redirect('expense')
            else:
                form.add_error(None, 'All fields are required.')
    else:
        form = ExpenseForm()
    return render(request, 'expense/add_expense.html', {'form': form})