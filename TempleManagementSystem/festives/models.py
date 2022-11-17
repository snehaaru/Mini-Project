from django.db import models

# Create your models here.
class Festives(models.Model):
    fid = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=20)
    startsdate = models.CharField(max_length=20)
    enddate = models.CharField(max_length=20)
    about = models.CharField(max_length=500)
    spclpooja = models.CharField(max_length=500)
    opentime = models.CharField(max_length=20)
    image = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'festives'
