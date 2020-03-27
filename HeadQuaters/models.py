from django.db import models

# Create your models here.
class HQinfo(models.Model):
    HQ_id=models.CharField(max_length=20)
    HQ_pass = models.CharField(max_length=50)
    HQ_name = models.CharField( max_length=50)
    HQ_location = models.CharField(max_length=50)
    HQ_email = models.EmailField( max_length=254)

    def __str__(self):
        return self.HQ_id+'    -     '+self.HQ_name

class Maindb(models.Model):
    db_name = models.CharField(max_length=50)
    db_ph_no = models.DecimalField( max_digits=10,decimal_places=0)
    db_email = models.EmailField(max_length=254)
    db_crime_subject = models.CharField( max_length=50)
    db_crime_description = models.TextField()
    db_more_info = models.TextField(null=True,blank=True)
    db_case_solved = models.BooleanField(default=False)

    def __str__(self):
        return self.db_crime_subject +'    -     ' + str(self.db_case_solved)
    