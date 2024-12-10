from django.urls import path
from . import views  # Import the views module

urlpatterns = [
    path('', views.expense_list, name='expense_list'),
    path('add/', views.index, name='add_expense'),
    path('docs/<str:doc_name>/', views.dynamic_doc, name="dynamic_doc"),
]