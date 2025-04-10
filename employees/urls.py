from django.urls import path
from . import views

app_name = 'employees'

urlpatterns = [
    path('', views.emp_list, name='emp_list'),
    path('add/', views.add_emp, name='add_emp'),
    path('edit/<int:pk>/', views.edit_emp, name='edit_emp'),
    path('delete/<int:pk>/', views.delete_emp, name='delete_emp'),
]