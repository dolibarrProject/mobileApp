from rest_framework import serializers
from .models import PointOfSale, Moral, Physical

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
