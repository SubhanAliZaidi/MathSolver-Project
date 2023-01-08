Naziya = "naziya"
from django.db import models

# Create your models here.

class Standarddeviation(models.Model):
    firstinput = models.CharField(max_length=99999999999999999999999999)
    secondinput = models.CharField(max_length=99999999999999999999999999, null=True)


class ContactForm(models.Model):
    name = models.CharField(max_length = 30)
    email = models.CharField(max_length = 30)
    phonenumber = models.CharField(max_length = 30, null=True)
    message = models.CharField(max_length = 99999999999)
    
    def __str__(self):
        return self.name


class Combinedinput(models.Model):
    combinedfirstinput = models.CharField(max_length=999999999999999)
    combinedsecondinput = models.CharField(max_length=999999999999999)
    combinedthirdinput = models.CharField(max_length=999999999999999)
    combinedfourthinput = models.CharField(max_length=999999999999999)
