from django import forms
from django.core.exceptions import ValidationError
from .models import Expense


class ExpenseForm(forms.ModelForm):
    """
    Form for adding or editing an expense.
    """
    class Meta:
        """
        **Model**: :model:`Expense`

        **Fields**:

        1. ``item``: Text field for entering the item name.
        2. ``amount``: Number field for entering the expense amount.
                        Accepts up to two decimal values.
        3. ``currency``: Dropdown field to select the currency.
        """
        model = Expense
        fields = ['item', 'amount', 'currency']
        """
        **Widgets**:

        1. ``item``: TextInput with a placeholder for entering the item name.
        2. ``amount``: NumberInput with a placeholder for entering the amount
             and constraints for minimum value and step.
        3. ``currency``: Select field with a
             placeholder for selecting the currency.
        """
        widgets = {
                'item': forms.TextInput(
                    attrs={'placeholder': 'Enter item'}
                    ),
                'amount': forms.NumberInput(
                    attrs={'placeholder': 'Enter amount', 'min': '0', 'step': '0.01'}
                    ),
                'currency': forms.Select(
                    attrs={'placeholder': 'Enter currency'}
                    ),
            }
