from django.shortcuts import render
from django.http import HttpResponse
def Patients(request):
    return HttpResponse("Details of the patent will be displayed here")
def patientshtml(request):
    template = loader.get_template('patents.html')
    return HttpResponse(template.render())

# Create your views here.

