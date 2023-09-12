from django.db import models

# Create your models here.
class ContactForm(models.Model):
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phone=models.CharField(max_length=15)
    age=models.CharField(max_length=15)

    def __str__(self):
        return self.firstname