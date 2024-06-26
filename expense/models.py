from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Expense(models.Model):
    """
    Model representing an expense in the app.

    **Meta**:

    - ``ordering``: Expenses are ordered in descending
    order based on the amount field.

    **Methods**:

    - ``__str__()``: Returns a human-readable string
    of the expense, displaying the item name.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.CharField(max_length=30)
    currency_choices = [
        ('USD', 'USD'),
        ('EUR', 'EUR'),
        ('GBP', 'GBP'),
        ('JPY', 'JPY'),
        ('AUD', 'AUD'),
        ('CAD', 'CAD'),
        ('CHF', 'CHF'),
    ]
    currency = models.CharField(
        max_length=3,
        choices=currency_choices,
        default='USD'
        )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
        )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-amount"]

    def __str__(self):
        return self.item
