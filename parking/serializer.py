from rest_framework import serializers

from parking.models import Client, Vehicle, ParkingSpot, Transaction


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'cpf', 'phone_number']


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['id', 'id_client', 'license_plate', 'car_model', 'colour', 'vehicle_type']


class ParkingSpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingSpot
        fields = ['id', 'price_hour', 'id_vehicle']


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id_client', 'id_vehicle', 'id_parking_spot', 'check_in', 'check_out']
