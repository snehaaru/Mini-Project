from django.db import models

# Create your models here.
class Temple(models.Model):
    tid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)

    place = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    prathishta = models.CharField(max_length=50)
    estd = models.CharField(db_column='Estd', max_length=5)  # Field name made lowercase.
    history = models.CharField(max_length=500)
    image = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'temple'
