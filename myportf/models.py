from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    message = models.CharField( max_length=100)
    
    def __str__(self):
        return self.name
    