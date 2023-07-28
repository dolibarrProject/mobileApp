from rest_framework import viewsets
from .models import *
from .serializers import *

class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer

class CredentialsViewSet(viewsets.ModelViewSet):
    queryset = Credentials.objects.all()
    serializer_class = CredentialsSerializer

class CitiesViewSet(viewsets.ModelViewSet):
    queryset = Cities.objects.all()
    serializer_class = CitiesSerializer

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
