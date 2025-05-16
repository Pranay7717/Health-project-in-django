from django.urls import path
from patents.views import Patients
from patents.views import patientshtml

urlpatterns = [
    path('patents/',Patients, name='Patients'),
    path('patients/',patientshtml, name ='patients-html')
]
