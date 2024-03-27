from django.db import models

# Create your models here.

class Contact(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Phone = models.CharField(max_length=10)
    Address = models.CharField(max_length=100)
    Comments = models.CharField(max_length=500,null=False)

    def __str__(self):
        return self.Name