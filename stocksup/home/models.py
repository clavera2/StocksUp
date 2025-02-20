from django.db import models

# Create your models here.
class User(models.Model):
    '''REPRESENTS A USER THAT CAN LOGIN AND TRACK STOCKS'''
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    