from rest_framework import serializers
from .models import Users, Credentials, Contract 


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class CredSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credentials
        fields = ['credentialId', 'userName', 'password']


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'