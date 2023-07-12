from django.db import models


# Create your models here.
class User(models.Model):
    userID = models.BigAutoField(primary_key=True)
    contractID = models.ForeignKey('Contract', on_delete=models.CASCADE)
    userName = models.ForeignKey('Credentials', on_delete=models.CASCADE)
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
    groupReference = models.CharField(max_length=100)#vendeur prevendeur liveur 
    # what is this?
    assignedRegion = models.ForeignKey('City', on_delete=models.CASCADE)
    teamSize = models.IntegerField()
    # could be a foreign key to department table, would be better


class City(models.Model):

    cityName = models.CharField(max_length=100, primary_key=True)
    cityRegion = models.CharField(max_length=100)
    #city region could be an enum since we have only 12 regions


class Magazinier(User):
    ismail = models.EmailField()
    # fake field, not in the database


class Warehouse(models.Model):
    warehouseID = models.BigAutoField(primary_key=True)
    warehouseLocation = models.CharField(max_length=100)
    warehouseCapacity = models.IntegerField()#pallets m3
    maxCapacity = models.IntegerField()