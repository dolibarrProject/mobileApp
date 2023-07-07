from django.db import models

# Create your models here.
class user(models.Model):
    userID = models.BigAutoField(primary_key=True)
    contractID = models.ForeignKey('contract', on_delete=models.CASCADE)
    userName = models.ForeignKey


class contract(models.Model):
    contractID = models.BigAutoField(primary_key=True)
    startDate = models.DateField()
    endDate = models.DateField()
    terms = (
        ('CDI','CDI'),
        ('CDD','CDD'),
        ('SESONIER', 'SESONIER'),
        ('EXTERN','EXTERN'),
    )

class Credentials(models.Model):
    credentialId = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=100)
    password = models.CharField(max_length=100)