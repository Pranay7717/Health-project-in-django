from django.urls import path
from . import views
app_name = 'patents'
urlpatterns = [
    path('patents/', views.Patients, name='Patients'),
]