from django.db import models

class Contract(models.Model):
    TERMS_CHOICES = (
        ('CDI', 'CDI'),
        ('CDD', 'CDD'),
        ('SESONIER', 'SESONIER'),
        ('EXTERN', 'EXTERN'),
    )

    contractID = models.BigAutoField(primary_key=True)
    startDate = models.DateField()
    endDate = models.DateField()
    terms = models.CharField(max_length=10, choices=TERMS_CHOICES)

class Credentials(models.Model):
    credentialId = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

class Cities(models.Model):
    cityId = models.AutoField(primary_key=True)
    cityName = models.CharField(max_length=100, unique=True)

class Users(models.Model):
    userId = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    telephone = models.CharField(max_length=20)
    cityAddress = models.CharField(max_length=100)
    creatDate = models.DateField()
    updateDate = models.DateField()
    terms = models.ForeignKey(Contract, on_delete=models.CASCADE, null=True)
    userName = models.ForeignKey('Credentials', on_delete=models.CASCADE)

class Seller(Users):
    salesRegion = models.CharField(max_length=100)
    supervised = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='seller_supervisor')

    

class Supervisor(Users):
    groupReference = models.IntegerField()
    teamSize = models.IntegerField()
    cityName = models.ForeignKey(Cities, on_delete=models.CASCADE, related_name='supervisor_city')

class PreSeller(Users):
    salesTarget = models.FloatField()
    commissionRate = models.FloatField()
    supervised = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='preseller_supervisor')


class DeliveryGuy(Users):
    vehiculeId = models.ForeignKey('Vehicule', on_delete=models.CASCADE, null=True)
    cityName = models.ForeignKey(Cities, on_delete=models.CASCADE, related_name='delivery_guy_city')
    supervised = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='delivery_guy_supervisor')


class Storekeeper(Users):
    storekeeperId = models.AutoField(primary_key=True)
    addressWarehouse = models.ForeignKey('Warehouse', on_delete=models.CASCADE, null=True)


class Vehicule(models.Model):
    vehiculeId = models.AutoField(primary_key=True)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    licensePlate = models.CharField(max_length=20)
    numChassis = models.CharField(max_length=100)

class Warehouse(models.Model):
    UNITY_CHOICES = (
        ('m3', 'm3'),
        ('m2', 'm2'),
        ('PALETTE', 'PALETTE'), 
    )
        
    warehouseId = models.BigAutoField(primary_key=True)
    addressWarehouse = models.CharField(max_length=200)
    cityName = models.ForeignKey(Cities, on_delete=models.CASCADE)
    capacity = models.IntegerField()
    maxCapacity = models.IntegerField()
    unity = models.CharField(max_length=10, choices=UNITY_CHOICES)


class PointOfSale(models.Model):
    posId = models.AutoField(primary_key=True)
    address = models.CharField(max_length=200)
    cityName = models.ForeignKey(Cities, on_delete=models.CASCADE)
    cashierName = models.CharField(max_length=100)


class Moral(PointOfSale):
    organizationName = models.CharField(max_length=100)


class Physical(PointOfSale):
    storeName = models.CharField(max_length=100)


class Category(models.Model):
    categoryId = models.AutoField(primary_key=True)
    categoryName = models.CharField(max_length=100)


class Product(models.Model):
    productId = models.AutoField(primary_key=True)
    productName = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    categoryName = models.ForeignKey(Category, on_delete=models.CASCADE)

class Order(models.Model):
    orderId = models.AutoField(primary_key=True)
    orderDate = models.DateField()
    productName = models.ForeignKey(Product, on_delete=models.CASCADE)
    orderTime = models.TimeField()
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    # product, data, time, vender

class OrderCard(models.Model):
    orderCardId = models.AutoField(primary_key=True)
    orderCardDate = models.DateField()
    totalAmount = models.DecimalField(max_digits=10, decimal_places=2)
    orderId = models.ForeignKey(Order, on_delete=models.CASCADE)
    vehiculeId = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    posId = models.ForeignKey(PointOfSale, on_delete=models.CASCADE)
