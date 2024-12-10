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
    try:
        if request.method == 'POST':
            form = ExpenseForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('expense_list')
        else:
            form = ExpenseForm()
        return render(request, 'tracker/index.html', {'form': form})
    except Exception as e:
        print("Error in index view:", e)
        return render(request, 'tracker/error.html', {'error': str(e)})
