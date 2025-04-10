from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee
from .forms import EmployeeForm

def emp_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees/emp_list.html', {'employees': employees})

def add_emp(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employees:emp_list')
    else:
        form = EmployeeForm()
    return render(request, 'employees/add_emp.html', {'form': form})

def edit_emp(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employees:emp_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employees/edit_emp.html', {'form': form})

def delete_emp(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employees:emp_list')
    return render(request, 'employees/delete_emp.html', {'employee': employee})
