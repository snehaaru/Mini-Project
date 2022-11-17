from django.db import models

# Create your models here.
class Ureg(models.Model):
    u_id = models.AutoField(primary_key=True)
    uname = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=15)
    nakshathra = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    dob = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    cpassword = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'ureg'
