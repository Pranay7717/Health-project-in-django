from django.db import models

class patents(models.Model):
    firstname = models.CharField(max_length =220)
    lastname = models.CharField(max_length = 220)
class doctors(models.Model):
    firstname = models.CharField(max_length =220)
    lastname = models.CharField(max_length = 220)
    
    

# Create your models here.
