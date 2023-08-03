from django.contrib import admin
from .models import Student, Major


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin) : 
    list_dispaly = ('std_id', 'prefix', 'name', 'lastname', 'phone')
    search_fields = ('name', 'lastname')


