from django.shortcuts import render, HttpResponse
from . import models

# Create your views here.
def home(request):
    context = {}

    students = models.Student.objects.all().order_by("id")

    context['Student'] = students

    return render(request,'index.html', context)
   # return HttpResponse("This it my django website")

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def studentDetail(request, id):
    context = ()
    students = models.Student.objects.filter(id=id)
    for student in students:
       context['student'] = student
    return render(request, 'details.html')