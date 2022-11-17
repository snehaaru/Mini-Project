from django.db import models

class Darshanabook(models.Model):
    da_id = models.AutoField(primary_key=True)
    date = models.CharField(max_length=65)
    time = models.TimeField()
    ppls = models.IntegerField()
    name = models.CharField(max_length=110)
    address = models.CharField(max_length=100)
    id_proof = models.CharField(max_length=100)
    id_number = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=100)
    date_of_birth = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    star = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'darshanabook'



class BookingTemp(models.Model):
    booking_id = models.AutoField(primary_key=True)
    did = models.IntegerField()
    u_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'booking_temp'


