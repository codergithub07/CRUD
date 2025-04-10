# Generated by Django 5.2 on 2025-04-10 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('department', models.CharField(choices=[('Engineering', 'Engineering'), ('Marketing', 'Marketing'), ('Finance', 'Finance'), ('HR', 'Human Resources'), ('IT', 'Information Technology')], max_length=100)),
                ('hire_date', models.DateField()),
                ('salary', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
