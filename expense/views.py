from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Sum
from django.contrib import messages
from django import forms
from .models import Expense
from .forms import ExpenseForm

# Create your views here.
"""

"""
@login_required
def index(request):
    expenses = Expense.objects.filter(user=request.user)
    total_amount = expenses.aggregate(total=Sum('amount'))['total']  # Calculate total amount for the user

    return render(request, "expense/index.html", {
        "expenses": expenses,
        "total_amount": total_amount,
    })


"""

"""
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


"""

"""
@login_required
def edit_expense(request, edit_id):
    expense = get_object_or_404(Expense, pk=edit_id, user=request.user)

    if request.method == "POST":
        expense_form = ExpenseForm(data=request.POST, instance=expense)
        if expense_form.is_valid():
            expense_form.save()
            messages.success(request, 'Expense Updated!')
            return HttpResponseRedirect(reverse('index'))
        else:
            messages.error(request, 'Error updating expense!')

    else:
        expense_form = ExpenseForm(instance=expense)

    return render(request, 'expense/edit_expense.html', {'form': expense_form, 'edit_id': edit_id})


########################################################################################################################
@login_required
def delete_expense(request, expense_id):
    expense = get_object_or_404(Expense, pk=expense_id, user=request.user)
    if request.method == "POST":
        expense.delete()
        messages.success(request, 'Expense deleted successfully!')
        return redirect('index')
    return redirect('index')