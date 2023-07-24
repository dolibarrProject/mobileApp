from django.urls import path

from . import views

urlpatterns = [
    path('', views.apiOverview),
    path('user-list/', views.userList, name="user-list"),
    # Credentials
    path('cred-create/', views.credCreate, name="cred-create"),
    path('cred-list', views.credList),
    path('cred-detail/<str:pk>/', views.credDetail),
    path('cred-update/<str:pk>/', views.credUpdate),
    path('cred-delete/<str:pk>/', views.credDelete),
    # to be tested
    # Contract
    path('contract-create/', views.contractCreate, name="contract-create"),
]
