from django.db import models
from doctors.models import  Doctors
from hospitals.models import  Hospitals
from disease.models import Disease

# Create your models here.
class Patients(models.Model):
    Patients_Num = models.IntegerField(primary_key=True, max_length=10)
    Name = models.CharField(max_length=20, blank=True, null=True)
    Address = models.TextField(max_length=50)
    Contacts= models.CharField(max_length=10, blank=True, null=True)

    Doctor =  models.ForeignKey(Doctors,on_delete=models.CASCADE)
    Hospital = models.ForeignKey(Hospitals,on_delete=models.CASCADE)
    Disease = models.ForeignKey(Disease, on_delete=models.CASCADE,)

    photo = models.FileField(upload_to='media', null=True, blank=True)

    class Meta:
        db_table = "Patients"