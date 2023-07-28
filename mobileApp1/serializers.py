from rest_framework import serializers
from .models import *

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'

class CredentialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credentials
        fields = '__all__'

class CitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields = '__all__'

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = '__all__'

class SupervisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supervisor
        fields = '__all__'

class PreSellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreSeller
        fields = '__all__'

class DeliveryGuySerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryGuy
        fields = '__all__'

class StorekeeperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storekeeper
        fields = '__all__'

class VehiculeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicule
        fields = '__all__'

class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = '__all__'

class PointOfSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PointOfSale
        fields = '__all__'

class MoralSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moral
        fields = '__all__'

class PhysicalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Physical
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderCard
        fields = '__all__'
