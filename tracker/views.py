from django.shortcuts import render, redirect
from .models import Expense
from .forms import ExpenseForm


def expense_list(request):
    try:
        expenses = Expense.objects.all()
        return render(request, 'tracker/expense_list.html', {'expenses': expenses})
    except Exception as e:
        print("Error in expense_list view:", e)
        return render(request, 'tracker/error.html', {'error': str(e)})


def index(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()  # Save the data if valid
            return redirect('index')  # Redirect after submission
    else:
        form = ExpenseForm()  # Initialize an empty form

    return render(request, 'tracker/index.html', {'form': form})
