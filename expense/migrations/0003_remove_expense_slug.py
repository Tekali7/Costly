# Generated by Django 5.0.4 on 2024-04-19 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0002_rename_name_expense_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='slug',
        ),
    ]
