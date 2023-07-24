from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ContractSerializer, UserSerializer, CredSerializer
from .models import Users, Credentials, Contract


def index(request):

    # Page from the theme
    return render(request, 'index.html')
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/user-list/',
        'Detail View':'/user-detail/<str:pk>/',
        'Create':'/user-create/',
        'Update':'/user-update/<str:pk>/',
        'Delete':'/user-delete/<str:pk>/',
        }
    return Response(api_urls)

@api_view(['GET'])
def userList(request):
    users = Users.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def userDetail(request, pk):
    users = Users.objects.get(id=pk)
    serializer = UserSerializer(users, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def userCreate(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['PUT'])
def userUpdate(request, pk):
    users = Users.objects.get(id=pk)
    serializer = UserSerializer(instance=users, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def userDelete(request, pk):
    users = Users.objects.get(id=pk)
    users.delete()
    return Response("Item successfully deleted")




# CREDANTIALS

@api_view(['POST'])
def credCreate(request):
    serializer = CredSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['GET'])
def credList(request):
    cred = Credentials.objects.all()
    serializer = CredSerializer(cred, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def credDetail(request, pk):
    cred = Credentials.objects.get(credentialId=pk)
    serializer = CredSerializer(cred, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def credUpdate(request, pk):
    cred = Credentials.objects.get(credentialId=pk)
    serializer = CredSerializer(instance=cred, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def credDelete(request, pk):
    cred = Credentials.objects.get(credentialId=pk)
    cred.delete()
    return Response("Item successfully deleted")

# Contract 

@api_view(['GET'])
def contractList(request):
    contract = Contract.objects.all()
    serializer = ContractSerializer(contract, many=True)
    return Response(serializer.data)

@api_view(['POST']) # not working
def contractCreate(request):
        serializer = ContractSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

@api_view(['GET'])
def contractDetail(request, pk):
    contract = Contract.objects.get(contractID=pk)
    serializer = ContractSerializer(contract, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def contractUpdate(request, pk):
    contract = Contract.objects.get(contractID=pk)
    serializer = ContractSerializer(instance=contract, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def contractDelete(request, pk):
    contract = Contract.objects.get(contractID=pk)
    contract.delete()
    return Response("Item successfully deleted")
