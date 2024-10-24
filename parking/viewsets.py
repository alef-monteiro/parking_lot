from rest_framework import viewsets, permissions

from parking.filters import ClientFilter, VehicleFilter, ParkingSpotFilter, TransactionFilter
from parking.models import Client, Vehicle, ParkingSpot, Transaction
from parking.serializer import ClientSerializer, VehicleSerializer, ParkingSpotSerializer, TransactionSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    filter_class = ClientFilter
    serializer_class = ClientSerializer
    permissions_classes = [permissions.IsAuthenticated]

    def create(self, resquest, *args, **kwargs):
        return super().create(resquest, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    filter_class = VehicleFilter
    serializer_class = VehicleSerializer
    permissions_classes = [permissions.IsAuthenticated]

    def create(self, resquest, *args, **kwargs):
        return super().create(resquest, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class ParkingSpotViewSet(viewsets.ModelViewSet):
    queryset = ParkingSpot.objects.all()
    filter_class = ParkingSpotFilter
    serializer_class = ParkingSpotSerializer
    permissions_classes = [permissions.IsAuthenticated]

    def create(self, resquest, *args, **kwargs):
        return super().create(resquest, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    filter_class = TransactionFilter
    serializer_class = TransactionSerializer
    permissions_classes = [permissions.IsAuthenticated]

    def create(self, resquest, *args, **kwargs):
        return super().create(resquest, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
