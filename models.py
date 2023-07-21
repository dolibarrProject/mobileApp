from django.db import models

class PointOfSale(models.Model):
    id = models.CharField(max_length=100)
    posId = models.CharField(max_length=100)
    location = models.CharField(max_length=100)  
    cashierName = models.CharField(max_length=100)
    category = models.CharField(max_length=100)

    class Meta:
        unique_together = ['id', 'posId']  

class Moral(PointOfSale):
    moralId = models.CharField(max_length=100)
    organizationName = models.CharField(max_length=100)

    class Meta:
        unique_together = ['id', 'moralId'] 

class Physical(PointOfSale):
    physicalId = models.CharField(max_length=100)
    storeName = models.CharField(max_length=100)

    class Meta:
        unique_together = ['id', 'physicalId'] 
