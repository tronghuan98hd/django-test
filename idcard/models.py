from django.db import models

# Create your models here.

class idCard(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=10)

    class Meta:
        db_table = 'idCard'