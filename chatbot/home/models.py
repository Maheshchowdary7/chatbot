from django.db import models

# Create your models here.

class Users(models.Model):
    UserName = models.CharField(max_length=15)
    Password = models.CharField(max_length=15)
    Mail = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'Users'