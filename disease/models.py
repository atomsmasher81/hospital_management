from django.db import models

# Create your models here.
class Disease(models.Model):
    disease_id = models.IntegerField(primary_key=True, )
    Name = models.CharField(max_length=20, blank=True, null=True)
    Symptoms = models.CharField(max_length=50)
    description = models.CharField(max_length=50)


    class Meta:
        db_table = "Disease"