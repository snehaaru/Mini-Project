from django.db import models
from ureg.models import Ureg

# Create your models here.
class Donation(models.Model):
    do_id = models.AutoField(primary_key=True)
    do_type = models.CharField(max_length=30)
    amount = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    # u_id = models.IntegerField()
    u=models.ForeignKey(Ureg,to_field='u_id',on_delete=models.CASCADE)
    status = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'donation'
