from rest_framework import routers

from parking.viewsets import ClientViewSet, VehicleViewSet, ParkingSpotViewSet, TransactionViewSet

routers = routers.DefaultRouter()

routers.register('client', ClientViewSet)
routers.register('vehicle', VehicleViewSet)
routers.register('parking_spot', ParkingSpotViewSet)
routers.register('transaction', TransactionViewSet)

urlpatterns = routers.urls
