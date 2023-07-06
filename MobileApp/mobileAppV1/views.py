from rest_framework import viewsets
from .models import Contract, Credentials, Users, Seller, Supervisor, PreSeller, DeliveryGuy, Storekeeper, Vehicule, Warehouse, PointOfSale, Moral, Physical, Category, Product, Order, OrderCard
from .serializers import ContractSerializer, CredentialsSerializer, UsersSerializer, SellerSerializer, SupervisorSerializer, PreSellerSerializer, DeliveryGuySerializer, StorekeeperSerializer, VehiculeSerializer, WarehouseSerializer, PointOfSaleSerializer, MoralSerializer, PhysicalSerializer, CategorySerializer, ProductSerializer, OrderSerializer, OrderCardSerializer

class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer

class CredentialsViewSet(viewsets.ModelViewSet):
    queryset = Credentials.objects.all()
    serializer_class = CredentialsSerializer

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class SellerViewSet(viewsets.ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer

class SupervisorViewSet(viewsets.ModelViewSet):
    queryset = Supervisor.objects.all()
    serializer_class = SupervisorSerializer

class PreSellerViewSet(viewsets.ModelViewSet):
    queryset = PreSeller.objects.all()
    serializer_class = PreSellerSerializer

class DeliveryGuyViewSet(viewsets.ModelViewSet):
    queryset = DeliveryGuy.objects.all()
    serializer_class = DeliveryGuySerializer

class StorekeeperViewSet(viewsets.ModelViewSet):
    queryset = Storekeeper.objects.all()
    serializer_class = StorekeeperSerializer

class VehiculeViewSet(viewsets.ModelViewSet):
    queryset = Vehicule.objects.all()
    serializer_class = VehiculeSerializer

class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer

class PointOfSaleViewSet(viewsets.ModelViewSet):
    queryset = PointOfSale.objects.all()
    serializer_class = PointOfSaleSerializer

class MoralViewSet(viewsets.ModelViewSet):
    queryset = Moral.objects.all()
    serializer_class = MoralSerializer

class PhysicalViewSet(viewsets.ModelViewSet):
    queryset = Physical.objects.all()
    serializer_class = PhysicalSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderCardViewSet(viewsets.ModelViewSet):
    queryset = OrderCard.objects.all()
    serializer_class = OrderCardSerializer
