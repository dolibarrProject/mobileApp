from django.db import models


# Create your models here.
class User(models.Model):
    userID = models.BigAutoField(primary_key=True)
    contractID = models.ForeignKey('contract', on_delete=models.CASCADE)
    userName = models.ForeignKey('credentials', on_delete=models.CASCADE)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField()
    userAddress = models.CharField(max_length=100)
    userCity = models.CharField(max_length=100)
    userPhoneNumber = models.CharField(max_length=100)
    creationDate = models.DateField()
    updateDate = models.DateField()


class Contract(models.Model):
    contractID = models.BigAutoField(primary_key=True)
    startDate = models.DateField()
    endDate = models.DateField()
    terms = (
        ('CDI', 'CDI'),
        ('CDD', 'CDD'),
        ('SESONIER', 'SESONIER'),
        ('EXTERN', 'EXTERN'),
    )


class Credentials(models.Model):
    # the username is the primary key
    userName = models.CharField(max_length=100, unique=True, primary_key=True)
    password = models.CharField(max_length=100)


class Supervisor(User):
    groupRefence = models.CharField(max_length=100)
    # what is this?
    assignedRegion = models.CharField(max_length=100)
    # could be a foreign key to region table, would be better
    teamSize = models.IntegerField()
    department = models.CharField(max_length=100)
    # could be a foreign key to department table, would be better


class Magazinier(User):
    ismail = models.EmailField()
    # fake field, not in the database


class Warehouse(models.Model):
    warehouseID = models.BigAutoField(primary_key=True)
    warehouseLocation = models.CharField(max_length=100)
    warehouseCapacity = models.IntegerField() 
    # ?? capacity of what? boolean?