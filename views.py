from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import PointOfSale, Moral, Physical
from .serializers import PointOfSaleSerializer, MoralSerializer, PhysicalSerializer

# CRUD API functions for PointOfSale model
@api_view(['GET', 'POST'])
def point_of_sale_list(request):
    if request.method == 'GET':
        pos_objects = PointOfSale.objects.all()
        serializer = PointOfSaleSerializer(pos_objects, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PointOfSaleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def point_of_sale_detail(request, ID, pos_id):
    try:
        pos_object = PointOfSale.objects.get(id=ID, posId=pos_id)
    except PointOfSale.DoesNotExist:
        return Response({"error": "Point of Sale not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PointOfSaleSerializer(pos_object)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PointOfSaleSerializer(pos_object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        pos_object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# CRUD API functions for Moral model
@api_view(['GET', 'POST'])
def moral_list(request, ID):
    if request.method == 'GET':
        moral_objects = Moral.objects.filter(id=ID)
        serializer = MoralSerializer(moral_objects, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        request.data['id'] = ID  # Add the id to the request data
        serializer = MoralSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def moral_detail(request, ID, moral_id):
    try:
        moral_object = Moral.objects.get(id=ID, moralId=moral_id)
    except Moral.DoesNotExist:
        return Response({"error": "Moral not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MoralSerializer(moral_object)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MoralSerializer(moral_object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        moral_object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# CRUD API functions for Physical model
@api_view(['GET', 'POST'])
def physical_list(request, ID):
    if request.method == 'GET':
        physical_objects = Physical.objects.filter(id=ID)
        serializer = PhysicalSerializer(physical_objects, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        request.data['id'] = ID 
        serializer = PhysicalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def physical_detail(request, ID, physical_id):
    try:
        physical_object = Physical.objects.get(id=ID, physicalId=physical_id)
    except Physical.DoesNotExist:
        return Response({"error": "Physical not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PhysicalSerializer(physical_object)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PhysicalSerializer(physical_object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        physical_object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
