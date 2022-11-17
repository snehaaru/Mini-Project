from django.db import models

# Create your models here.
class Report(models.Model):
    rid = models.AutoField(primary_key=True)
    caption = models.CharField(max_length=50)
    about = models.CharField(max_length=500)
    report = models.CharField(max_length=20)
    date = models.CharField(max_length=20)
    time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'report'
