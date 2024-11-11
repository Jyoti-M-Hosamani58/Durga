from django.db import models

# Create your models here.



class Login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    utype=models.CharField(max_length=50)



class contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    message = models.CharField(max_length=15)

    def __str__(self):
        return self.full_name
