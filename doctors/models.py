from django.db import models
from hospitals.models import  Hospitals
# Create your models here.
class Doctors(models.Model):
    Enroll_Num = models.IntegerField(primary_key=True, )
    Name = models.CharField(max_length=20, blank=True, null=True)
    Contacts= models.CharField(max_length=10, blank=True, null=True)
    Qualification = models.TextField(max_length=5, blank=True, null=True)
    Hospital = models.ForeignKey(Hospitals,on_delete=models.CASCADE)
    photo = models.FileField(upload_to='media',null=True,blank=True)


    class Meta:
        db_table = "Doctors"

