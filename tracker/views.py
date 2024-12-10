from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from .models import Expense
from .forms import ExpenseForm


def expense_list(request):
    if request.method != "GET":
        return HttpResponseBadRequest("Invalid HTTP method.")  # Fix for 405 error
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
            return redirect('add_expense')  # Ensure the name matches your URL
    else:
        form = ExpenseForm()  # Initialize an empty form

    return render(request, 'tracker/index.html', {'form': form})


def dynamic_doc(request, doc_name):
    """
    Dynamically render HTML files located in 'docs/' safely
    by checking allowed filenames dynamically.
    """
    docs_path = 'tracker/templates/tracker'

    if doc_name in [f.split('.')[0] for f in os.listdir(docs_path)]:  # Dynamically validate
        return render(request, f'tracker/{doc_name}.html')
    else:
        return HttpResponseForbidden("You don't have permission to access this file.")
