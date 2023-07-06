from django.urls import include, path
from rest_framework import routers
from .views import ContractViewSet, CredentialsViewSet, UsersViewSet, SellerViewSet, SupervisorViewSet, PreSellerViewSet, DeliveryGuyViewSet, StorekeeperViewSet, VehiculeViewSet, WarehouseViewSet, PointOfSaleViewSet, MoralViewSet, PhysicalViewSet, CategoryViewSet, ProductViewSet, OrderViewSet, OrderCardViewSet

router = routers.DefaultRouter()
router.register('contracts', ContractViewSet)
router.register('credentials', CredentialsViewSet)
router.register('users', UsersViewSet)
router.register('sellers', SellerViewSet)
router.register('supervisors', SupervisorViewSet)
router.register('presellers', PreSellerViewSet)
router.register('deliveryguys', DeliveryGuyViewSet)
router.register('storekeepers', StorekeeperViewSet)
router.register('vehicles', VehiculeViewSet)
router.register('warehouses', WarehouseViewSet)
router.register('pointofsales', PointOfSaleViewSet)
router.register('morals', MoralViewSet)
router.register('physicals', PhysicalViewSet)
router.register('categories', CategoryViewSet)
router.register('products', ProductViewSet)
router.register('orders', OrderViewSet)
router.register('ordercards', OrderCardViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
