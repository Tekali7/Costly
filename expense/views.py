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
Renders the expense index page with a list of expenses 
and the sum of costs for the logged-in user.
User needs to be authenticated.

**Context**

``expenses``
    A queryset containing all expenses belonging to the logged-in user.

``total_amount``
    The total amount of expenses for the logged-in user.

**Template:**

:template:`expense/index.html`
"""
@login_required
def index(request):
    expenses = Expense.objects.filter(user=request.user)
    total_amount = expenses.aggregate(total=Sum('amount'))['total']

    return render(request, "expense/index.html", {
        "expenses": expenses,
        "total_amount": total_amount,
    })


"""
Allows logged-in users to add a new expense.
User needs to be authenticated.

**HTTP Methods**

- GET: Displays the expense form to add a new expense.
- POST: Processes the submitted expense form
        and adds a new expense to the database.

**Context**

``expense_form``
    An instance of :form:`ExpenseForm` for adding a new expense.

**Template:**

:template:`expense/add_expense.html`
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
Allows logged-in users to edit an existing expense.
User needs to be authenticated.

**HTTP Methods**

- GET: Displays the expense edit form for the chosen expense.
- POST: Processes the submitted expense edit form
        and updates the expense in the database.

**Context**

``form``
    An instance of :form:`ExpenseForm` for editing the expense.
    
``edit_id``
    The ID of the expense being edited.

**Template:**

:template:`expense/edit_expense.html`
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


"""
Allows logged-in users to delete an existing expense.
User needs to be authenticated.

**HTTP Methods**

- POST: Deletes the specified expense from the database.

**Redirect**
- Redirects to the expense index page (:view:`index`) after
  deletion of the chosen expense.

"""
@login_required
def delete_expense(request, expense_id):
    expense = get_object_or_404(Expense, pk=expense_id, user=request.user)
    if request.method == "POST":
        expense.delete()
        messages.success(request, 'Expense deleted successfully!')
        return redirect('index')
    return redirect('index')