from django.db import models

class Employee(models.Model):
    DEPARTMENT_CHOICES = [
        ('Engineering', 'Engineering'),
        ('Marketing', 'Marketing'),
        ('Finance', 'Finance'),
        ('HR', 'Human Resources'),
        ('IT', 'Information Technology'),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100, choices=DEPARTMENT_CHOICES)
    hire_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.department}"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
