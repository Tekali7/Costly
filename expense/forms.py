from django import forms
from django.core.exceptions import ValidationError
from .models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['item', 'amount', 'currency']
# add labels here later
    
    def clean_item(self):
        item = self.cleaned_data.get('item')
        if item.isdigit():
            raise ValidationError("Item cannot be a number, please use letters.")
        return amount


    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount <= 0:
            raise ValidationError("Amount must be a positive number.")
        return amount


    def clean(self):
        cleaned_data = super().clean()
        item = cleaned_data.get('item')
        amount = cleaned_data.get('amount')
        currency = cleaned_data.get('currency')

        if not item or not amount or not currency:
            raise ValidationError("All fields are required.")

        return cleaned_data
