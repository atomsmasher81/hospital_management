from django.db import models

# Create your models here.
class Hospitals(models.Model):
    Hospital_id = models.IntegerField(primary_key=True, max_length=10)
    Name = models.CharField(max_length=20, blank=True, null=True)
    Loaction = models.CharField(max_length=50, blank=True, null=True)
    Contact_num = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = "Hospital"