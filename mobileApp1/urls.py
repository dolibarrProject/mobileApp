from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

# Create a router and register your viewsets
router = DefaultRouter()
router.register(r'contracts', ContractViewSet)
router.register(r'credentials', CredentialsViewSet)
router.register(r'cities', CitiesViewSet)
router.register(r'users', UsersViewSet)
router.register(r'sellers', SellerViewSet)
router.register(r'supervisors', SupervisorViewSet)
router.register(r'presellers', PreSellerViewSet)
router.register(r'deliveryguys', DeliveryGuyViewSet)
router.register(r'storekeepers', StorekeeperViewSet)
router.register(r'vehicules', VehiculeViewSet)
router.register(r'warehouses', WarehouseViewSet)
router.register(r'pointofsales', PointOfSaleViewSet)
router.register(r'morals', MoralViewSet)
router.register(r'physicals', PhysicalViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'ordercards', OrderCardViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
