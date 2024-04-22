from django import forms
from django.core.exceptions import ValidationError
from .models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['item', 'amount', 'currency']
        widgets = {
                'item': forms.TextInput(attrs={'placeholder': 'Enter item'}),
                'amount': forms.NumberInput(attrs={'placeholder': 'Enter amount', 'min': '0', 'step': '0.01'}),
                'currency': forms.Select(attrs={'placeholder': 'Enter currency'}),
            }