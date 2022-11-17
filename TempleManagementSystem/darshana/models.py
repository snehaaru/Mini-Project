from django.db import models


class Darshana(models.Model):
    did = models.AutoField(primary_key=True)
    day = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    desc = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    price = models.CharField(max_length=100)


    class Meta:
        managed = False
        db_table = 'darshana'


class BookingTemp(models.Model):
    booking_id = models.AutoField(primary_key=True)
    # did = models.IntegerField()
    d=models.ForeignKey(Darshana,on_delete=models.ForeignKey)
    u_id = models.IntegerField()
    status = models.CharField(max_length=20)
    vb_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'booking_temp'


class Vazhipadbook(models.Model):
    vb_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    star = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    u_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'vazhipadbook'



