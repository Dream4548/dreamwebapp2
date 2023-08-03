from django.contrib import admin
from .models import Student, Major


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin) : 
    list_dispaly = ('')

# Register your models here.
