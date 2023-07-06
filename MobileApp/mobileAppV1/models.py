from django.db import models

class Contract(models.Model):
    contractId = models.AutoField(primary_key=True)
    startDate = models.DateField()
    endDate = models.DateField()
    terms = models.TextField()

class Credentials(models.Model):
    credentialId = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Users(models.Model):
    userId = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    telephone = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    creatDate = models.DateField()
    updateDate = models.DateField()
    contratId = models.ForeignKey(Contract, on_delete=models.CASCADE, null=True)

class Seller(Users):
    sallerId = models.AutoField(primary_key=True)
    salesRegion = models.CharField(max_length=100)

class Supervisor(Users):
    supervisorId = models.AutoField(primary_key=True)
    groupReference = models.CharField(max_length=100)
    assigncRegion = models.CharField(max_length=100)
    teamSize = models.IntegerField()
    department = models.CharField(max_length=100)

class PreSeller(Users):
    preSellerId = models.AutoField(primary_key=True)
    salesTarget = models.FloatField()
    commissionRate = models.FloatField()

class DeliveryGuy(Users):
    deliveryGuyId = models.AutoField(primary_key=True)
    deliveryRoute = models.CharField(max_length=100)
    vehiculeId = models.ForeignKey('Vehicule', on_delete=models.CASCADE, null=True)

class Storekeeper(Users):
    storekeeperId = models.AutoField(primary_key=True)
    invertoryManagmentSystem = models.CharField(max_length=100)
    warehouseLocation = models.ForeignKey('Warehouse', on_delete=models.CASCADE, null=True)

class Vehicule(models.Model):
    vehiculeId = models.AutoField(primary_key=True)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    licensePlate = models.CharField(max_length=20)
    year = models.IntegerField()

class Warehouse(models.Model):
    warehouseId = models.AutoField(primary_key=True)
    location = models.CharField(max_length=200)
    capacity = models.IntegerField()

class PointOfSale(models.Model):
    posId = models.AutoField(primary_key=True)
    location = models.CharField(max_length=200)
    cashierName = models.CharField(max_length=100)

class Moral(PointOfSale):
    moralId = models.AutoField(primary_key=True)
    organizationName = models.CharField(max_length=100)

class Physical(PointOfSale):
    physicalId = models.AutoField(primary_key=True)
    storeName = models.CharField(max_length=100)

class Category(models.Model):
    categoryId = models.AutoField(primary_key=True)
    categoryName = models.CharField(max_length=100)

class Product(models.Model):
    productId = models.AutoField(primary_key=True)
    productName = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    categoryId = models.ForeignKey(Category, on_delete=models.CASCADE)

class Order(models.Model):
    orderId = models.AutoField(primary_key=True)
    orderDate = models.DateField()

class OrderCard(models.Model):
    orderCardId = models.AutoField(primary_key=True)
    orderCardDate = models.DateField()
    totalAmount = models.DecimalField(max_digits=10, decimal_places=2)
    orderId = models.ForeignKey(Order, on_delete=models.CASCADE)
    vehiculeId = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    posId = models.ForeignKey(PointOfSale, on_delete=models.CASCADE)
