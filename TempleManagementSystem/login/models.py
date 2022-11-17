from django.db import models


class Login(models.Model):
    log_id = models.AutoField(primary_key=True)
    uname = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    u_type = models.CharField(max_length=20)
    u_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'login'
