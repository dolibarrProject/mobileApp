from django.db import router
from django.urls import include, path
from rest_framework.routers import DefaultRouter


from . import views

router = DefaultRouter()
router.register(r'cred-create', views.Cred, basename='cred-create')
router.register(r'contract-create', views.Cont, basename='contract-create')
router.register(r'users', views.User, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    # path('user-list/', views.userList, name="user-list"),
    # path('user-detail/<str:pk>/', views.userDetail, name="user-detail"),
    # path('user-create/', views.userCreate, name="user-create"),
    # path('user-update/<str:pk>/', views.userUpdate, name="user-update"),
    # path('user-delete/<str:pk>/', views.userDelete, name="user-delete"),

    # # Credentials
    # #path('cred-create/', views.credCreate, name="cred-create"),
    
    # path('cred-list', views.credList),
    # path('cred-detail/<str:pk>/', views.credDetail),
    # path('cred-update/<str:pk>/', views.credUpdate),
    # path('cred-delete/<str:pk>/', views.credDelete),
    # # to be tested
    # # Contract
    # path('contract-create/', views.contractCreate, name="contract-create"),
    # path('contract-list', views.contractList),
    # path('contract-detail/<str:pk>/', views.contractDetail),
    # path('contract-update/<str:pk>/', views.contractUpdate),
    # path('contract-delete/<str:pk>/', views.contractDelete),

]
