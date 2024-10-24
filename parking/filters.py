from django_filters import FilterSet, CharFilter, NumberFilter

from parking.models import Client, Vehicle, ParkingSpot, Transaction

EQUALS = 'exact',
LIKE = 'unaccent_icontains',
STARTSWITH = 'startswith',
GTE = 'gte',
GT = 'gt',
LTE = 'lte',
LT = 'lt',


class ClientFilter(FilterSet):
    id = NumberFilter(field_name='id', lookup_expr=EQUALS),
    name = CharFilter(field_name='name', loockup_expr=LIKE),
    cpf_sw = CharFilter(field_name='cpf', lookup_expr=STARTSWITH),
    cpf_eq = CharFilter(field_name='cpf', lookup_expr=EQUALS),
    phone_number_sw = CharFilter(field_name='phone_number', lookup_expr=STARTSWITH),
    phone_number_eq = CharFilter(field_name='phone_number', lookup_expr=EQUALS),

    class Meta:
        model = Client
        fields = ['id', 'name', 'cpf', 'phone_number']


class VehicleFilter(FilterSet):
    id = NumberFilter(field_name='id', lookup_expr=EQUALS),
    id_client = CharFilter(field_name='id_client__name', lookup_expr=LIKE),
    license_plate = CharFilter(field_name='license_plate', lookup_expr=LIKE),
    license_plate_sw = CharFilter(field_name='license_plate', lookup_expr=STARTSWITH),
    car_model = CharFilter(field_name='car_model', lookup_expr=LIKE),
    car_model_sw = CharFilter(field_name='car_model', lookup_expr=STARTSWITH),
    colour = CharFilter(field_name='colour', lookup_expr=LIKE),
    colour_sw = CharFilter(field_name='colour', lookup_expr=STARTSWITH),
    vehicle_type = CharFilter(field_name='vehicle_type', lookup_expr=LIKE),
    vehicle_type_sw = CharFilter(field_name='vehicle_type', lookup_expr=STARTSWITH),

    class Meta:
        model = Vehicle
        fields = ['id', 'id_client', 'license_plate', 'car_model', 'colour', 'vehicle_type']


class ParkingSpotFilter(FilterSet):
    price_hour = NumberFilter(field_name='price_hour', lookup_expr=LTE),
    id_vehcile = CharFilter(field_name='id_vehicle__name', lookup_expr=LIKE),
    id_vehcile_sw = CharFilter(field_name='id_vehicle__name', lookup_expr=STARTSWITH),

    class Meta:
        model = ParkingSpot
        fields = ['id', 'price_hour', 'id_vehicle']


class TransactionFilter(FilterSet):
    id_client = CharFilter(field_name='id_client__name', lookup_expr=LIKE)
    id_vehcile = CharFilter(field_name='id_vehicle__name', lookup_expr=LIKE),
    id_vehcile_sw = CharFilter(field_name='id_vehicle__name', lookup_expr=STARTSWITH),
    id_parking_spot = CharFilter(field_name='id_parking_spot', lookkup_expr=EQUALS),
    total_value = NumberFilter(field_name='total_value', lookup_expr='LTE'),

    class Meta:
        model = Transaction
        fields = ['id_client', 'id_vehicle', 'id_parking_spot']
