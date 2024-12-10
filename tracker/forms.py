from django import forms
from .models import Expense  # Ensure you have a model named Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['amount', 'description', 'date']  # Adjust fields based on your model