from django.db import models

# Create your models here.
class Userinfo(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField( max_length=254)
    ph_no = models.DecimalField(max_digits=10, decimal_places=0)
    crime_sub = models.CharField(max_length=50)
    date = models.DateField(auto_now=False, auto_now_add=False)
    def __str__(self):
        return self.name+'   -   '+self.crime_sub