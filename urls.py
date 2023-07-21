from django.urls import path
from . import views

urlpatterns = [
    # URLs for PointOfSale model
    path('pointofsale/', views.point_of_sale_list, name='point_of_sale_list'),
    path('pointofsale/<str:ID>/<str:pos_id>/', views.point_of_sale_detail, name='point_of_sale_detail'),

    # URLs for Moral model
    path('moral/<str:ID>/', views.moral_list, name='moral_list'),
    path('moral/<str:ID>/<str:moral_id>/', views.moral_detail, name='moral_detail'),

    # URLs for Physical model
    path('physical/<str:ID>/', views.physical_list, name='physical_list'),
    path('physical/<str:ID>/<str:physical_id>/', views.physical_detail, name='physical_detail'),
]
