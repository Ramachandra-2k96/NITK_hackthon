# myapp/models.py
from django.db import models
from django.contrib.auth.models import User
from django.db.models import F

class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    projects =models.CharField()
    date = models.DateTimeField()
    def __str__(self):
        return self.user.username

class Create_company(models.Model):
    Company_name =models.CharField(max_length=225)
    GSTIN =models.CharField(max_length=225)
    Created_date =models.DateField()  

    