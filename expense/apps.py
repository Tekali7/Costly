from django.apps import AppConfig


class ExpenseConfig(AppConfig):
    """
    Configuration for the 'expense' Django app.

    **Attributes**:

    - ``default_auto_field``: The default auto field for model primary keys.
    - ``name``: The name of the Django app, which is 'expense'.

    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'expense'
