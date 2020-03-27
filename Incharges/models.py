from django.db import models

# Create your models here.
class Inchargeinfo(models.Model):
    incharge_id = models.CharField(max_length=20)
    incharge_pass = models.CharField( max_length=50)
    name = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    def __str__(self):
        return self.incharge_id +'    -     '+self.name
    